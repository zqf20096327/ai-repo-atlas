# splunk/splunk-mltk-container-docker

⭐ 63 · Jupyter Notebook · Apache-2.0 · 推送 2026-10-30 · [GitHub](https://github.com/splunk/splunk-mltk-container-docker) · [官网](https://splunkbase.splunk.com/app/4607/) · 组织维护

**Splunk DSDL 应用的 ML 容器镜像构建与定制资源库**

该仓库提供 Splunk App for Data Science and Deep Learning（DSDL，原 DLTK）5.2.4 所用默认容器镜像的构建资源：容器端点代码、Jupyter 配置、示例 notebook、Dockerfile 与构建脚本，覆盖 TensorFlow、PyTorch、Transformers、RAPIDS、Spark、LLM RAG、Agentic AI 等 CPU/GPU 镜像配置。企业用户可通过 build.sh 与 tag_mapping.csv 定制、加固并重新构建镜像，扫描漏洞（Trivy）并运行 Playwright 测试，再以 images.conf 注册到 Splunk 环境中使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 10 种预置镜像构建标签（golden-cpu/gpu、transformers、RAPIDS、LLM RAG、Agentic AI 等）
- tag_mapping.csv 支持自定义 base image、Dockerfile、requirements 与 nvidia runtime 的组合扩展
- 附带 Trivy 漏洞扫描与 Playwright 容器测试脚本
- requirements 预编译脚本加速含大量 Python 依赖的镜像构建

## 适用场景

- 为企业环境定制并重建 DSDL 数据科学容器镜像
- 为 DSDL 增加新框架或 GPU 运行时的自定义镜像配置
- 对构建出的容器执行漏洞扫描与模拟测试

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L11: This repository contains the collection of resources, scripts, and testing frameworks that are used build and deplo
> L14: This repository contains the container endpoint (`./app`), jupyter notebook configuration (`./config`) and examples

## 星数曲线

```mermaid
xychart-beta
    title "splunk/splunk-mltk-container-docker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 62 --> 64
    line [63, 63]
```

2026-10-18 63 → 2026-10-31 63（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `bdc07923c5b3` · [字段定义](../../DATASET.md)*
