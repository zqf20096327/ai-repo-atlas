# 0xPlaygrounds/rig

⭐ 9,289 · Rust · MIT · 推送 2026-11-27 · [GitHub](https://github.com/0xPlaygrounds/rig) · [官网](https://rig.rs) · 组织维护

**Rust 库与终端编码 Agent：模块化构建 LLM 应用**

Rig 是一个用于构建大语言模型应用的 Rust 库，将 20 多个模型提供商和十余种向量存储统一在同一接口之后，支持带工具、流式输出与类型化钩子的 agent，覆盖 completion、embedding、转录、音频与图像模型，并遵循 OpenTelemetry GenAI 约定。库还附带基于其构建的终端编码 agent `rig`，其工具、命令、会话等均以 Bevy 插件形式可替换或扩展。`rig-core` 与 `rig-agent` 可构建为浏览器 WASM。运行需 Rust 1.97.1+，支持 Linux 与 macOS。

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

- 20+ 模型提供商与十余种向量存储统一接口
- 终端编码 agent `rig`，全部能力以插件形式可关闭/替换/扩展
- 支持 completion、embedding、转录、音频与图像模型
- rig-core 与 rig-agent 支持浏览器 WASM 构建

## 适用场景

- 用 Rust 构建调用多家模型提供商的 LLM 应用
- 扩展或定制终端编码 agent 的工具与命令
- 统一接入多种向量存储实现检索场景

## 场景标签

`Agent 框架` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L8: Rig is a Rust library for building applications on large language models.
> L54: Rig puts over 20 model providers and a dozen vector stores behind one
> L55: interface. It has agents with tools, streaming and typed hooks. It covers

## 星数曲线

```mermaid
xychart-beta
    title "0xPlaygrounds/rig 星数(近 27 点)"
    x-axis ["2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27", "2026-11-28"]
    y-axis "stars" 8931 --> 9321
    line [8967, 8981, 8996, 9003, 9018, 9027, 9029, 9035, 8963, 9094, 9109, 9114, 9129, 9141, 9147, 9154, 9161, 9166, 9180, 9190, 9203, 9214, 9219, 9240, 9265, 9280, 9289]
```

2026-10-26 8,967 → 2026-11-28 9,289（+322）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `0693a328ea19` · [字段定义](../../DATASET.md)*
