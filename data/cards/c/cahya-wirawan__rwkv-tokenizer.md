# cahya-wirawan/rwkv-tokenizer

⭐ 55 · Jupyter Notebook · Apache-2.0 · 推送 2026-07-26 · [GitHub](https://github.com/cahya-wirawan/rwkv-tokenizer) · [官网](https://github.com/cahya-wirawan/rwkv-tokenizer) · 个人维护

**Rust 实现的 RWKV World 分词器，含 Python/WASM 绑定**

用 Rust 编写的 RWKV 分词器库，支持 RWKV v5 及更新模型使用的 World Tokenizer。提供 Rust crate、Python 模块（pyrwkv-tokenizer）与 WebAssembly（Node.js/Web）三种绑定，支持批处理编码与多线程。README 报告与原版分词器在英文维基与中文诗歌数据集上编码结果一致并通过其单元测试，性能对比中给出倍数数据。另提供 json2bin 工具将 JSONL 数据集转为 RWKV 训练用的 binidx 格式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Rust 实现 RWKV World Tokenizer，支持 RWKV v5 及更新模型
- 提供 Rust/Python/WebAssembly 三种绑定
- 支持批处理编码与多线程
- 附带 json2bin 工具将 JSONL 转为 binidx 训练数据格式

## 适用场景

- 在 Rust/Python/Web 应用中对 RWKV 模型文本做分词
- 将 JSONL 数据集转换为 RWKV 训练所需的 binidx 格式
- 验证分词结果与原版 RWKV 分词器的一致性

## 场景标签

 · 领域:NLP/LLM 基础设施

## 证据(README 行号)

> L10: A fast RWKV Tokenizer written in Rust that supports the World Tokenizer used by the
> L11: RWKV v5 and newer models.

## 星数曲线

```mermaid
xychart-beta
    title "cahya-wirawan/rwkv-tokenizer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 54 --> 56
    line [55, 55]
```

2026-10-18 55 → 2026-10-28 55（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `adb5f5a1321e` · [字段定义](../../DATASET.md)*
