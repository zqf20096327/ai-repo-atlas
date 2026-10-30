# 1amageek/swift-gigatoken

⭐ 30 · Swift · MIT · 推送 2026-07-31 · [GitHub](https://github.com/1amageek/swift-gigatoken) · 个人维护

**纯 Swift 实现的 Byte-level BPE 分词器，面向高性能 LLM 分词路径**

受 Marcel Roed 的 gigatoken 启发的独立 Swift 实现，提供 Byte-level BPE 编码/解码，兼容基线为 r50k_base，与参考实现输出相同的 token ID。核心为 Foundation-free 的 GigaTokenCore，支持 Apple ARM64 NEON/CRC32 加速、WebAssembly 与 Embedded Swift，采用零拷贝输入输出、可复用 TokenBuffer 与缓存感知查找。通过 Swift Package 构建，需指定的 Swift 6.4 开发快照工具链；基准为单机实测，非通用吞吐保证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 零拷贝输入输出与可复用 TokenBuffer 的性能数据路径
- NEON/CRC32 编译期门控原生内核，附带 Pure Swift 可移植实现
- 支持 Native、WebAssembly 与 Embedded Swift 构建
- 与参考实现 r50k_base 输出 token ID 完全一致的校验夹具

## 适用场景

- LLM 推理流水线中替换分词热路径
- MLX Swift / Core AI 等张量运行时直接消费连续 UInt32 token ID
- Wasm 与嵌入式环境无 Foundation 依赖的 BPE 分词

## 场景标签

 · 领域:LLM 基础设施/分词

## 证据(README 行号)

> L3: Byte-level BPE tokenization with a Pure Swift portable data path for Native,
> L82: - Contiguous `UInt32` token access for MLX Swift, Core AI, and other runtimes.
> L148: For MLX Swift, Core AI, or another tensor runtime, depend on `TokenEncoding`

## 星数曲线

```mermaid
xychart-beta
    title "1amageek/swift-gigatoken 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-30"]
    y-axis "stars" 28 --> 31
    line [29, 30, 30]
```

2026-10-18 29 → 2026-10-30 30（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `e75d47a2378c` · [字段定义](../../DATASET.md)*
