# data.pephub
Data stores for the [pephub](https://github.com/pepkit/pephub) server. All PEPs hosted with pephub can be located here. New PEP's are added via pull requests to this repository.

## Repository Structure
All PEPs are stored in the following format: `{namespace}/{project}`. PEP's are stored inside individual namespace folders that represent teams/organizations/labs. Inside each namespace will be folders that correspond to each unique PEP:

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
To facilitate the generalization of data storage and allow users to stick to their own naming conventions, a `.pephub.yaml` file can be included inside indidual PEP folders to specify the PEP `project_config.yaml` file.

```yaml
config_file: path/to/file.yaml
```
*Note: If a `.pephub.yaml` file is not specified, pephub will simply search for a `project_config.yaml` file instead, as this is the default naming convention used in the PEP documentation. As such, you can choose to omit the `.pephub.yaml` file and stick with naming your config files `project_config.yaml`.*


## Contributing a PEP
If you would like to contribute a PEP, please do so by forking this repository and creating a pull-request where the PEP will be verified and merged.