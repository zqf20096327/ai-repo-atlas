# scalattice/scalattice-agent

⭐ 11 · Rust · NOASSERTION · 推送 2026-11-20 · [GitHub](https://github.com/scalattice/scalattice-agent) · [官网](https://scalattice.com) · 组织维护

**GPU 提供者的接入代理：把本地 GPU 接入 Scalattice 推理网络接单**

Scalattice 推理网络（Robottik Ltd 产品）的 GPU agent：在有 GPU 的机器上安装、用 provider token 连接后，Scalattice Cloud 可将推理任务路由到该机器。单二进制以三角色运行（supervisor、每计算设备一个 slot worker、托盘面板），支持 Linux/Windows/macOS，覆盖 NVIDIA/AMD/Intel/Apple Silicon/CPU 后端，后台以 systemd/LaunchAgent/scheduled task 常驻，日志轮转 8 MiB。Intel Mac 不支持；AMD/Intel 经 Vulkan，无需 ROCm。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单二进制三角色进程树：supervisor、按设备的 slot worker、托盘控制面板
- 后端覆盖 CUDA（NVIDIA）、Vulkan（AMD/Intel/ARM）、Metal（Apple Silicon）、CPU
- 子进程与 supervisor 生命周期绑定（PR_SET_PDEATHSIG/Job Object/LaunchAgent watchdog）
- 提供 Linux 脚本安装、Windows/macOS 安装包及 Rust/Cargo 源码构建

## 适用场景

- 把闲置 GPU 机器注册为 Scalattice 网络的推理提供者
- 多 GPU 机器上按设备运行推理 worker 并集中管理
- 跨 Linux/Windows/macOS 部署常驻 GPU 代理服务

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L5: GPU agent for the Scalattice inference network,
> L8: Install it on a machine with a GPU, connect with a provider token, and Scalattice Cloud can route inference jobs to 
> L117: The agent connects to Scalattice Cloud using the built-in endpoint. Region, models, and schedule are managed in th

## 星数曲线

```mermaid
xychart-beta
    title "scalattice/scalattice-agent 星数(近 3 点)"
    x-axis ["2026-10-19", "2026-11-14", "2026-11-21"]
    y-axis "stars" 9 --> 12
    line [10, 11, 11]
```

2026-10-19 10 → 2026-11-21 11（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-18 · 置信度 high · 依据 README sha `50ca1c75e0fc` · [字段定义](../../DATASET.md)*
