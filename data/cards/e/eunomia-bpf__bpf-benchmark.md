# eunomia-bpf/bpf-benchmark

⭐ 26 · C · MIT · 推送 2026-10-28 · [GitHub](https://github.com/eunomia-bpf/bpf-benchmark) · 组织维护

**LLM Agent 做 eBPF 优化的闭环评测基准与自动研究框架**

bpf-bench 将 eBPF 优化定义为 LLM agent 的闭环搜索问题：agent 选择优化动作（源码修改、LLVM/字节码变换、bpfopt 策略、内核 JIT 与 Kinsn 原生操作），框架在 Docker/KVM/AWS 隔离环境中对真实应用执行动作，每轮返回 verifier、JIT、工作负载与性能反馈。语料含 6 个生产 eBPF 应用、146 个可比较 BPF 程序测量与 42 个微基准任务，并带完整性检查防止 reward hacking。同时是 ATC'26 论文 BPF-Ext 的 artifact 工作区。以 git clone 源码方式获取，需 Python3、Docker、virtme-ng 等前置条件，通过根 Makefile 运行各 suite。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 闭环 agent 优化：动作执行于真实应用与工作负载（Docker/KVM/AWS 隔离环境）
- 覆盖 6 个生产 eBPF 应用、146 个 BPF 程序测量、42 个微基准任务
- 反馈包含 verifier 接受/拒绝日志、JIT 输出、负载正确性与内核计数器
- Agent 完整性模型：agent 须通过 make 目标交互，框架记录原始产物供外部判定

## 适用场景

- 评测 LLM agent 在真实 verifier/JIT 约束下做 eBPF 优化的决策能力
- 复现 ATC'26 BPF-Ext/Kinsn 论文的实验与数据
- 作为 agentic 内核扩展优化的自动研究执行底座

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L44: `bpf-bench` frames eBPF optimization as a closed-loop search problem for LLM
> L72: `bpf-bench` evaluates whether agents can make better optimization decisions
> L90: `bpfopt` and Kinsn-backed native operations are action backends in this

## 星数曲线

```mermaid
xychart-beta
    title "eunomia-bpf/bpf-benchmark 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-29"]
    y-axis "stars" 24 --> 27
    line [25, 26, 26]
```

2026-10-18 25 → 2026-10-29 26（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `c7829baebfc9` · [字段定义](../../DATASET.md)*
