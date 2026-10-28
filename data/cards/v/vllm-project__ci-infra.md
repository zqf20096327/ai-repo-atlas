# vllm-project/ci-infra

⭐ 61 · Python · Apache-2.0 · 推送 2026-10-27 · [GitHub](https://github.com/vllm-project/ci-infra) · 组织维护

**vLLM 项目的 CI 与性能基准基础设施代码仓库**

为 vLLM 持续集成流水线提供的基础设施即代码与引导脚本：基于 Buildkite，在 AWS（EC2 自动伸缩、ECR/S3 缓存、热缓存 AMI）与 GCP（GKE GPU 节点池、TPU v5/v6e/v7x）上调度 CI 任务。核心组件为 Python 流水线生成器，读取 vLLM 仓库的 YAML 步骤定义并生成带 Docker/Kubernetes 插件的 Buildkite 流水线；支持 CPU、L4/A100/H100/H200/B200、Intel HPU、AMD MI 系列、Ascend NPU 等设备类型。供 vLLM 项目维护者与贡献者使用，修改需联系维护者获取分支权限。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Python 流水线生成器：读取 vLLM 仓库 YAML 步骤定义并生成 Buildkite 流水线
- Terraform 管理 AWS/GCP 基础设施，含自动伸缩 agent 队列与 TPU 节点
- 多层缓存策略：Docker 层缓存（ECR）、热缓存 AMI、sccache、预编译 wheel
- 支持 CPU/GPU（L4/A100/H100/H200/B200）、Intel、AMD、Ascend、ARM 等设备类型

## 适用场景

- 维护者修改 vLLM CI 流水线与基础设施配置
- 新增 CI runner 或专用硬件队列（K8s agent/Elastic CI Stack/独立 agent）
- 通过分支环境变量 VLLM_CI_BRANCH 测试 CI 改动

## 场景标签

 · 领域:CI/CD 与云基础设施

## 证据(README 行号)

> L3: Infrastructure-as-Code and bootstrap scripts for vLLM's continuous integration pipeline, built on Buildkite with aut
> L42: A Python tool (`buildkite/pipeline_generator/`) that reads step definitions from YAML files in the vLLM repo (e.g. 

## 星数曲线

```mermaid
xychart-beta
    title "vllm-project/ci-infra 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 60 --> 62
    line [61, 61]
```

2026-10-18 61 → 2026-10-28 61（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `ad1f4cbd4108` · [字段定义](../../DATASET.md)*
