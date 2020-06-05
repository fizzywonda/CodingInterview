"""
Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of
projects, where the second project is dependent on the first project). All of a project's dependencies
must be built before the project is. Find a build order that will allow the projects to be built. If there
is no valid build order, return an error.
EXAMPLE
Input:
projects: a, b, c, d, e, f
dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
Output: f, e, a, b, d, c
"""

class Node:
    def __init__(self, a):
        self.data = a
        self.dependencies = {}

class Graph:
    def __init__(self, project_list, dependency_list):
        self.projects = {}
        for node in project_list:
            self.projects[node.data] = node
        self.add_edge(dependency_list)

    def add_edge(self, dependency_list):
        for start, end in dependency_list:
            start_node = self.projects[start]
            end_node = self.projects[end]
            end_node.dependencies[start] = start_node

    def build_order(self):
        order = []
        for project in self.projects.values():
            if len(project.depencies.values()) == 0:
                order.append(project)
                self.remove_dependant(project)
        return order

    def remove_dependant(self, dependant):
        for project in self.projects.values():
            if dependant.data in project.depencies:
                del project.depencies[dependant.data]



