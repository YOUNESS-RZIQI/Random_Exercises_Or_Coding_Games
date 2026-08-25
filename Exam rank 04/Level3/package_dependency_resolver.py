"""
Description of the Kahn's algorithm
Kahn’s algorithm is a well-known approach for computing
a topological ordering of a directed acyclic graph (DAG).
The main idea is to process the graph by always selecting nodes
that have no incoming edges, which means they do not depend
on any other nodes. At the beginning, the algorithm computes
the in-degree of each node, defined as the number of edges
entering that node. All nodes with an in-degree of zero are placed
into a queue or set. The algorithm then repeatedly removes
one node from this set, appends it to the topological order,
and removes all of its outgoing edges from the graph.
When an outgoing edge is removed, the in-degree of the destination
node is decreased; if this in-degree becomes zero, the node is
added to the set.
The algorithm continues until there are no nodes left to process.
If all nodes are included in the result, the graph is acyclic and
the ordering is valid;
otherwise, the presence of remaining edges indicates a cycle.

"""

"""
Theory

1. Subject Analysis & Implementation Strategy
In this problem, packages are "nodes" and dependencies are
directional "edges." If "app" depends on "database", you have
an edge pointing from "database" to "app" (meaning database
must be processed first).

The chosen algorithm: Kahn's Algorithm (Modified)
Kahn’s algorithm is the standard way to find a topological sort.
It works by tracking the "in-degree" of every node—which in this
context means "how many unresolved dependencies does this package
have?"

Find the starting line: Identify all packages with an in-degree
of 0 (they need nothing else to be installed).

Process and unlock: "Install" those packages. For every package
you install, look at the packages that depend on it and reduce
their in-degree by 1.

Queue the next batch: If any of those dependent packages reach
an in-degree of 0, they are now ready to be installed.
Add them to your queue.

Cycle detection: If the queue empties but you haven't installed
every package, it means the remaining packages are locked
in a circular dependency (e.g., A needs B, B needs A).

The Alphabetical Catch (Breadth-First Sorting):
The example output for independent chains
(["api", "web", "backend", "frontend"])
is a major hint. If you use a strict priority queue (min-heap),
"backend" would process before "web" because 'b' comes before 'w'.
To get the example's output, we must use a FIFO queue
(Breadth-First Search approach) where we sort packages in batches
as they become available at the same depth level.
"""

"""
Implementation

Explanation:
https://www.youtube.com/watch?v=cIBFEhD77b4&t=10s

Topological Sort
A linear ordering of vertices or nodes in
a graph where for every directed edge from vertex U to vertex V,
vertex U comes before V in the ordering.
- only possible in Directed Acyclic Graphs (DAGs), which is a graph
    without directed cycles
- a graph with cycling vertices can't have a topological sort.
- multiple valid topological sorts can exist for a graph


Indegree
The number of directed edges coming into that vertex.
Indegree of 0: no depedencies - immediate installation is possible.


Kahn's Algorithm
1) Compute indegrees: iterate through the graph, count indegrees
for every node.
2) Queue zeros: identify nodes with 0 indegree and
push them into Queue
3) Process graph: pop from Queue, add to result, reduce
neighbor indegrees.
Repeat.

Detection of circular dependencies:
The beauty of Kahn's Algorithm is that packages trapped in a cycle
never make it into the queue in the first place. Because they
are waiting on each other, neither of them ever reaches
0 dependencies, so the algorithm just leaves them behind.

Let's use your example: packages = {"A": ["B"], "B": ["A"]}.

Calculate In-degrees:

A depends on B, so A's in-degree is 1.

B depends on A, so B's in-degree is 1.

State: in_degree = {"A": 1, "B": 1}

Find the Starting Line (The Queue):

The code says: if in_degree[pkg] == 0: queue.append(pkg)

Is A's in-degree 0? No, it's 1.

Is B's in-degree 0? No, it's 1.

State: queue = [] (It is completely empty).

Process the Queue:

The code says: while len(queue) > 0:

Because the queue is already empty, the while loop never runs.
It gets skipped entirely.

State: result = [] (It never had a chance to append anything).

Cycle Detection:

The code says: if len(result) == len(packages):

len(result) is 0.

len(packages) is 2.

0 == 2 is False, so the code hits the else block and returns [].


While loop engine:
Think of the while loop as processing packages in distinct batches or waves.

The Two Lists
queue: The packages we are installing right now (the current wave).

next_queue: The packages that are being unlocked while we install
the current wave. We can't install them yet because we haven't finished
the current wave, so we set them aside here.

The Step-by-Step Cycle
Let's look at the example:
{"app": ["database"], "database": ["driver"], "driver": []}

Wave 1:

The while loop starts. queue is ["driver"].

We create an empty next_queue = [].

We install "driver". This drops the in-degree of "database" to 0.

Because "database" is now unlocked, we append it to next_queue.

The for loop finishes. We have successfully installed everything in Wave 1.

The Handoff:
At this exact moment:

queue is still ["driver"] (which we already processed).

next_queue is ["database"] (which is waiting to be processed).

If we just loop back to the top of the while loop without changing
anything, we would be stuck in an infinite loop installing "driver"
over and over again!

By executing queue = next_queue, we are passing the baton. We are
telling Python: "We are done with the old wave. Make the newly unlocked
packages the active queue for the next loop."

Wave 2:

The while loop evaluates len(queue). Because we swapped the lists,
queue is now ["database"].

The loop runs again, processing "database", which unlocks "app",
adding "app" to the new next_queue.

The baton is passed again (queue = next_queue).

How the Loop Finally Stops
Eventually, we will process a wave that unlocks absolutely
nothing (like "app" at the very end).
When that happens, next_queue remains empty [].
We do queue = next_queue, which means queue becomes [].
The while loop checks len(queue) > 0, sees that it is 0,
and finally ends.



Why we have to use two queues instread of one with .pop()/append()
Yes, you can absolutely use a single list as a queue without
importing anything.

Standard Python lists have a built-in .pop(0) method that removes
and returns the first element.So, why didn't we use a single
continuous queue with queue.pop(0) and queue.append()?

There are two reasons—one involves performance, but the more
important one is a hidden trap in your exam's rules.1.
The Exam Trap: The "Alphabetical" Rule
The subject states: "process packages alphabetically when choices
exist".

When you have parallel, independent chains, a standard single
queue processes dependencies in the order their parents were
processed, not alphabetically.
Lets look at a scenario that breaks the single-queue approach.
Imagine this input:{"A": [], "B": [], "Z": ["A"], "Y": ["B"]}
(A unlocks Z. B unlocks Y. A and B are independent).
If we use a single continuous queue:
Start: queue = ["A", "B"]Pop "A".
This unlocks "Z". We append "Z".queue is now ["B", "Z"].
Pop "B". This unlocks "Y". We append "Y".queue is now ["Z", "Y"].
Pop "Z", then pop "Y".
Output: ["A", "B", "Z", "Y"]
Did you spot the error?
Z and Y both became fully unlocked at the exact same time
(after the first wave of A and B finished).
Because choices existed, they should have been processed
alphabetically.
The correct output must be ["A", "B", "Y", "Z"].
Why our "Wave" approach fixes this:
By using next_queue, we gather everything that unlocks during
a single level, sort it all together, and only then make it
the active queue.
Wave 1 processes "A" and "B". next_queue collects "Z" and "Y".
We sort next_queue to ["Y", "Z"].
Wave 2 processes them in perfect alphabetical order.
2. The Performance Reason
While you can use list.pop(0) to remove the first item of a list,
it is notoriously slow in Python. When you use .pop(0), Python has
to take every single remaining item in the list and shift it one
position to the left in memory. If your queue has 10,000 items,
popping the first one requires moving 9,999 items. Doing this in
a loop creates a massive performance bottleneck ($O(N^2)$ time
complexity).The deque object from the collections module exists
specifically to solve this—its .popleft() method is instantaneous
($O(1)$). But since your exam forbids imports, our "wave" approach
(for current in queue) is brilliant because we just iterate over
the list normally, avoiding the expensive .pop(0) entirely!
"""


def package_dependency_resolver(
        packages: dict[str, list[str]]) -> list[str]:
    # Guard-rails
    if len(packages) == 0:
        return []

    # Initialize trackers
    graph: dict[str, list[str]] = {}
    indegrees: dict[str, int] = {}

    # Set zeros for all package indegrees
    for pkg in packages:
        graph[pkg] = []
        indegrees[pkg] = 0

    # Build the graph with reversed values
    # graph:

    for pkg, deps in packages.items():
        valid_count = 0

        for dep in deps:
            # processing only existent deps
            if dep in packages:
                valid_count += 1
                # installing dep before pkg
                graph[dep].append(pkg)
        # record count of valid deps to indegrees dict
        indegrees[pkg] = valid_count

    # Find the starting line
    # Find pkgs with 0 indeegries and sort them
    queue = []

    for pkg in packages:
        if indegrees[pkg] == 0:
            queue.append(pkg)
    # sort alphabetically for deterministic output
    queue.sort()

    # Process the queue
    # Every package is already in graph.
    # We access nodes simply graph[current]

    result = []

    # reversed logic pkg: dep -> 'driver': ['database']
    while len(queue) > 0:
        next_queue = []
        # current = 'driver'
        for current in queue:
            result.append(current)

            # update indeegres
            # pkg = 'database' in graph['driver']
            for pkg in graph[current]:
                indegrees[pkg] -= 1

                # ready pkg add to next wave next_queue
                if indegrees[pkg] == 0:
                    next_queue.append(pkg)

        # sort next_queue and assign it to queue
        next_queue.sort()
        # queue had 'driver', which got copied to result
        # now queue is replaced by 'database'
        # process continues till 'app', which has no deps
        # then len(queue) will be 0, loop breaks
        queue = next_queue

    # Cycle detection and output
    if len(result) == len(packages):
        return result
    else:
        return []


print("# Dependencies: driver → database → app")
res = package_dependency_resolver(
    {"app": ["database"],
     "database": ["driver"],
     "driver": []})
print("expected: [\"driver\", \"database\", \"app\"]")
print(f"output: {res}\n")

print("# A has no deps, B needs A, C needs both A and B")
res = package_dependency_resolver(
    {"A": [],
     "B": ["A"],
     "C": ["A", "B"]})
print("expected: [\"A\", \"B\", \"C\"]")
print(f"output: {res}\n")

print("# Empty input")
res = package_dependency_resolver({})
print("expected: []")
print(f"output: {res}\n")

print("# Circular dependency: X needs Y, Y needs X")
res = package_dependency_resolver(
    {"X": ["Y"],
     "Y": ["X"]})
print("expected: []")
print(f"output: {res}\n")

print("# Two independent chains: api→backend and web→frontend")
res = package_dependency_resolver(
    {"web": [],
     "api": [],
     "frontend": ["web"],
     "backend": ["api"]})
print("expected: [\"api\", \"web\", \"backend\", \"frontend\"]")
print(f"output: {res}")
