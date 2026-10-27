# dimzachar/DataTalksClub-Projects

⭐ 25 · Python · MIT · 推送 2026-05-05 · [GitHub](https://github.com/dimzachar/DataTalksClub-Projects) · [官网](https://datatalksclub-projects.streamlit.app/) · 个人维护

**抓取并分析 DataTalksClub 课程项目提交的 Streamlit 应用**

面向 DataTalksClub 课程社区的工具：流水线自动发现已结束课程、抓取项目提交的 GitHub 仓库，拉取 10 类关键文件（docker-compose、Terraform、DAG、requirements 等），再用 LLM（经 OpenRouter）基于实际代码生成描述性标题，并分类部署类型（Batch/Streaming）与云厂商（GCP/AWS/Azure），结果写入 CSV 并以 Streamlit 仪表盘展示。支持并行处理（默认 5 workers）、按课程/年份/单仓库处理与失败重试；提供在线实例与 Docker 运行两种查看方式。运行流水线需 GitHub Token 与 OpenRouter API Key；本地开发要求 Python 3.11（3.12+ 存在依赖问题）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 抓取每个仓库 10 类关键文件（非仅 README）供 LLM 分析
- LLM 生成描述性标题并分类部署类型与云厂商，输出分类依据
- 并行处理（默认 5 workers）与按课程/年份/单仓库粒度的处理选项
- 提供 Streamlit 在线仪表盘与 Docker 本地运行两种查看途径

## 适用场景

- 浏览 DataTalksClub 各课程的学生项目并按部署类型/云厂商筛选
- 课程组织者批量梳理项目提交情况
- 数据工程学习者按领域（如 NYC Taxi 管道）查找参考项目

## 场景标签

`网页抓取` `数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L11: DataTalksClub-Projects automates the analysis of projects from DataTalksClub courses. It scrapes project submission
> L40: 4. **LLM Classification** - Analyzes actual code to determine:
> L43: 5. **Title Generation** - Creates descriptive titles based on:

## 星数曲线

```mermaid
xychart-beta
    title "dimzachar/DataTalksClub-Projects 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-27 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `12b05d028c6b` · [字段定义](../../DATASET.md)*
