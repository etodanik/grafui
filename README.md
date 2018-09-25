# grafui

grafui is a cross platform graphical user interface for grpah databases built in Qt for Python. The first version is going to only support `neo4j` as a database, however there shouldn't be any reason not to support other databases in the future.

__*At this moment this repository is in extremely early development stages and is not ready for any kind of use*__

## Motivation

Every mature database out there has various graphical user interfaces to help manage and query data.

However, at the time of writing this readme, I could not find anything at all for graph databases. 

## Roadmap for first pre-alpha release
_Checked items are implemented_
- [x] Basic connection management
  - [x] Adding / removing connections
  - [x] Storing connections in operation system registry
  - [x] Storing passwords separately in encrypted keychain storage 
- [ ] Workspaces
  - [x] Initiating a connection
  - [ ] Creating a workspace tab for the newly opened connection
  - [ ] Query editor and runner
  - [ ] Table view for retrieved records
    - [ ] Sorting
    - [ ] Pagination
  - [ ] Graph view for retrieved records
    - [ ] Node visualization
    - [ ] Relationship visualization
    - [ ] Traversing / expanding nodes by double clicking
- [ ] Elementary CRUD
  - [ ] Editing properties on retrieved records
  - [ ] Creating new nodes
  - [ ] Removing existing nodes
- [ ] Relationships
  - [ ] Displaying relationships
  - [ ] Editing properties on relationships
  - [ ] Creating new relationships between nodes
  - [ ] Removing existing relationships
- [ ] Indicies and constraints
  - [ ] Listing indicies and constraints
  - [ ] Creating / editing / removing indicies and constraints
- [ ] Discovery and metrics
  - [ ] Fetching a list of node labels
  - [ ] Fetching a list of relationship types
  - [ ] Fetching a list of property keys
  - [ ] Showing metrics for database
  
## Development

```bash
git clone https://github.com/israelidanny/grafui.git
cd grafui
pipenv install
./run.sh
```