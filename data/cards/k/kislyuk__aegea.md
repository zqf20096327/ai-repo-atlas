# kislyuk/aegea

⭐ 69 · Python · Apache-2.0 · 推送 2026-02-01 · [GitHub](https://github.com/kislyuk/aegea) · 个人维护

**面向 AWS 账户运维人员的命令行操作界面**

Python CLI 工具，为 AWS 账户运维人员提供命令与终端仪表盘：基于 cloud-init 构建 AMI 与 Docker 镜像、启动和监控 EC2 实例（spot/AMI/实例类型选项）、通过 SSM/EC2 Instance Connect 免开入站端口实现 SSH、提交与监控 AWS Batch 与 ECS Fargate 任务、查询 CloudWatch Logs 与 CloudTrail、查看成本报告及管理 Secrets Manager。配置经多层 JSON/YAML 来源递归合并，支持数组合并操作符。README 提及可与 MiniWDL 配合编排 MLops 与基因组学工作流，但本体为 AWS 资源管理工具。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- cloud-init 驱动的 AMI 与 Docker 镜像构建
- aegea ssh 免入站端口连接并按名称解析实例地址
- AWS Batch 与 ECS Fargate 任务提交、监控与计算环境管理
- 多来源配置递归合并与数组操作符（$append/$extend）

## 适用场景

- 运维人员在终端管理 EC2、Batch、ECS 等 AWS 资源
- 免开入站端口通过 SSM 连接实例并传输文件
- 构建和复用基于 cloud-init 的机器镜像
- 在 AWS 上编排 MLops 与基因组学工作流

## 场景标签

 · 领域:云计算/运维工具

## 证据(README 行号)

> L3: *Aegea* is a command line interface (CLI) that provides a set of essential commands and terminal dashboards for
> L9: `MiniWDL <https://github.com/chanzuckerberg/miniwdl>`_ to orchestrate large-scale MLops and genomics workflows.

## 星数曲线

```mermaid
xychart-beta
    title "kislyuk/aegea 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 68 --> 70
    line [69, 69]
```

2026-10-18 69 → 2026-10-29 69（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 low · 依据 README sha `77fbfc61e189` · [字段定义](../../DATASET.md)*
