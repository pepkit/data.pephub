# data.pephub
Data stores for the [pephub](https://github.com/pepkit/pephub) server. All PEPs hosted with pephub can be located here. New PEP's are added via pull requests to this repository.

## Repository Structure
PEPs are stored in this reopsitory under a hierarchical folder structure, `{namespace}/{project}/`. Namespace folders represent teams/organizations/labs. Inside each namespace folder, individual folders correspond to each PEP. For example:

```
├── ChangLab
│   ├── PEP_1
│   │   ├── 180113_mergeTable.csv
│   │   ├── README.md
│   │   ├── TCGA_AllSamples_FinalBamList_annotation.csv
│   │   └── TCGA_AllSamples_FinalBamList_config.yaml
│   └── PEP_2
│       ├── 180113_mergeTable.csv
│       ├── README.md
│       ├── TCGA_AllSamples_FinalBamList_annotation.csv
│       └── TCGA_AllSamples_FinalBamList_config.yaml
└── demo
    ├── BiocProject
    │   ├── data
    │   │   ├── laminB1Lads.bed
    │   │   └── vistaEnhancers.bed
    │   ├── project_config.yaml
    │   ├── project_config_resize.yaml
    │   ├── readBedFiles.R
    │   ├── readBedFiles_resize.R
    │   └── sample_table.csv
    ├── BiocProject_exceptions
    │   ├── project_config.yaml
    │   ├── readBedFilesExceptions.R
    │   └── sample_table.csv
```

## The `.pephub.yaml` file
By default, pephub assumes the project config will be named `project_config.yaml` (`<namespace>/<project>/project_config.yaml`). Optionally, users may use their own file naming conventions by including a `.pephub.yaml` file inside the PEP folder. The `.pephub.yaml` file should specify location of the project config like this:

```yaml
config_file: path/to/file.yaml
```


## Contributing a PEP

If you would like to contribute a PEP, please do so by forking this repository and creating a pull-request where the PEP will be verified and merged.
