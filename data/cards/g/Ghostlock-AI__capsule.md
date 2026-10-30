# Ghostlock-AI/capsule

⭐ 28 · Rust · MIT · 推送 2026-01-05 · [GitHub](https://github.com/Ghostlock-AI/capsule) · [官网](https://ghostlock.ai) · 组织维护

**给自主 agent 的 Linux 内核级行为追踪与沙箱工具**

Rust 编写的 Linux（当前仅 aarch64）内核级追踪与沙箱项目，面向自主 agent 的行为可观测与约束。通过 eBPF kprobes/tracepoints/LSM 钩子捕获系统调用级事件，用户态守护进程做流式摄取与异步富化，生成人类可读的行为时间线；观测范围覆盖进程执行、网络、文件 I/O、凭证变更、内存映射、IPC、设备访问、容器/cgroup 与信号。策略层结合确定性规则与序列/图模型判定风险。自述处于 pre-alpha 阶段。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- eBPF/LSM 内核级捕获系统调用与语义事件
- 观测覆盖进程/网络/文件/凭证/内存/IPC/设备/容器等 10 类行为
- 策略层：确定性规则 + 序列/图模型风险分类
- 声明永久开源，不做双许可或闭源核心

## 适用场景

- 追踪长时间运行 agent 在系统调用层面的实际行为
- 生成可审计、不可规避的 agent 行为时间线
- 为 agent 执行环境构建内核级沙箱与策略约束

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L5: Capsule watches agent behavior from the kernel (eBPF/LSM), enriches events into human-readable timelines, and lays t
> L46: - **Kernel Probes**: eBPF kprobes/tracepoints/LSM hooks (Linux) capture syscall-level and semantic events.
> L48: - **Policy/ML Layer**: deterministic rules + sequence/graph model that categorizes prompt, syscall sequence, and re

## 星数曲线

```mermaid
xychart-beta
    title "Ghostlock-AI/capsule 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-30 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `9ad1388ea467` · [字段定义](../../DATASET.md)*
