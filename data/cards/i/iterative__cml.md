# iterative/cml

⭐ 4,191 · JavaScript · Apache-2.0 · 推送 2026-10-21 · [GitHub](https://github.com/iterative/cml) · [官网](http://cml.dev) · 组织维护

**面向 MLOps 的开源 CI/CD CLI 工具，自动训练评估模型并生成报告**

持续机器学习（CML）是开源命令行工具，在 GitLab/GitHub/Bitbucket 上实现面向 MLOps 的 CI/CD：自动化机器供给、模型训练与评估、跨历史比较 ML 实验与监控数据集变化。提供 cml runner 启动本地或云实例（AWS/Azure/GCP/Kubernetes）、以评论或检查形式向 PR 投递 Markdown 报告、自动创建 PR、连接 TensorBoard。报告可含图像、表格等；数据管理可搭配 DVC 与多种云存储。面向在 Git 平台上构建 ML 工作流的数据科学与工程团队。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- cml runner 可在 AWS/Azure/GCP/Kubernetes 上自动分配云实例（含 GPU）并在任务后自动关闭
- 自动生成含指标与图表的 Markdown 报告并投递到 PR 评论或 GitHub 检查
- 预装 Python/CUDA/git/node 的官方 Docker 镜像（含 GPU 标签）
- 支持 S3/Azure/Aliyun/Google Storage/Google Drive 等云存储配置

## 适用场景

- 每次 PR 自动训练模型并把指标与图表报告贴到评论
- 用云或本地 GPU 机器作为自托管 runner 训练模型
- 结合 DVC 管理数据并在提交间比较实验指标

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L4: **What is CML?** Continuous Machine Learning (CML) is an open-source CLI tool
> L6: MLOps. Use it to automate development workflows — including machine


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `351aeae74ac7` · [字段定义](../../DATASET.md)*
