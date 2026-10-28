# microsoft/dstoolkit-devcontainers

⭐ 51 · Python · MIT · 推送 2026-10-24 · [GitHub](https://github.com/microsoft/dstoolkit-devcontainers) · 组织维护

**微软维护的 ML 项目模板：多 Docker 开发容器与 CI 流水线**

基于 VSCode Dev Container 的机器学习与数据科学项目模板，支持在同一仓库内使用多个 Docker 容器环境（提供 CPU 与 GPU 示例），以 uv 管理 Python 依赖并用锁文件保证环境一致。内置 ruff 代码质量检查（保存时与 pre-commit 钩子）、pytest 配置、GitHub Actions 与 Azure DevOps CI 流水线模板，以及 Azure Machine Learning 云端训练示例，覆盖从本地实验到云端训练的过渡。给数据科学团队用于统一环境搭建与提升代码质量。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同一仓库内多个 Docker Dev Container（CPU/GPU 示例）
- uv 管理依赖，锁文件保证各容器构建版本一致
- ruff 自动化代码质量检查（VSCode 保存时与 pre-commit）
- GitHub Actions 与 Azure DevOps CI 流水线模板及 AML 云端示例

## 适用场景

- 数据科学团队统一本地与云端开发环境
- 在同一项目中并行实验多种 Python 环境
- 将本地训练流程迁移到 Azure Machine Learning
- 为 ML 项目配置带测试与覆盖率报告的 CI 流水线

## 场景标签

 · 领域:机器学习工程/MLOps

## 证据(README 行号)

> L11: This repository provides a VSCode Dev Container based project template that can help accelerate your Machine Learni
> L13: During the early phase of Machine Learning project, you may face challenges such as each data scientist creating va

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/dstoolkit-devcontainers 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-28 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `6c709a7d1cc3` · [字段定义](../../DATASET.md)*
