# yanghao1143/rust-norion

⭐ 19 · Rust · GPL-3.0 · 推送 2026-07-16 · [GitHub](https://github.com/yanghao1143/rust-norion) · 个人维护 · 中文 README

**DNA 启发的本地 LLM 推理控制层/自进化控制引擎研究原型**

Rust 实现的推理控制层原型，处理路由、层级调度、KV/gist 记忆、反思、经验回放与设备适配等推理外层逻辑，而非训练完成的推理内核。支持内置 local runtime、command runtime、manifest/设备门禁与远程 Gemma 链路适配；自进化以 preview/gate/rollback 门禁为主，不默认放开持久 mutation。项目自述为非生产可用的研究工程仓库，GPLv3 许可，面向非商业研究部署，需从 Rust 源码构建运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 可运行的控制层原型：本地启发式后端、benchmark/gate、服务协议验证
- ModelRuntime/InferenceBackend 后端接入边界与 RuntimeManifest 设备契约验证
- 记忆模块管理 KV、gist、经验、语义索引与写入门禁
- 自进化以 preview/gate/rollback 为主，强调证据与审计

## 适用场景

- 研究推理控制层的路由、记忆与反思机制
- 在统一边界后接入本地或外部 runtime 做实验
- 验证自进化门禁与设备契约的工程实现

## 场景标签

 · 领域:LLM 基础设施/推理运行时

## 证据(README 行号)

> L6: “北极星”（`rust-norion`）是一个 DNA 启发的 Rust 推理控制层 / 自进化控制引擎原型。
> L11: - 一个可运行的控制层原型：能跑本地启发式后端、状态检查、benchmark/gate 和服务协议验证。
> L88: - `InferenceBackend`：控制层调用真实后端的最小抽象。

## 星数曲线

```mermaid
xychart-beta
    title "yanghao1143/rust-norion 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-31"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-31 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `7927367f3737` · [字段定义](../../DATASET.md)*
