# Michael-A-Kuykendall/shimmytok

⭐ 25 · Rust · Apache-2.0 · 推送 2026-10-18 · [GitHub](https://github.com/Michael-A-Kuykendall/shimmytok) · [官网](https://docs.rs/shimmytok) · 个人维护

**纯 Rust 的 GGUF 分词器库：直接从模型文件读取并运行 tokenizer**

以纯 Rust 实现的 tokenizer 库，直接从 GGUF 模型文件中提取并运行内嵌的分词器，无需 C++ FFI、Python 或额外 tokenizer 文件，输出与 llama.cpp 一致（逐 token 验证）。支持 SPM/BPE/WPM/UGM/RWKV 五类算法与 41 种 BPE 预分词正则；提供批量编码（可选 Rayon 并行，WASM/WASI 下降级为顺序执行且结果确定性）、流式解码与元数据查询 API。MIT OR Apache-2.0 双许可，声明永久免费，提供赞助层级。

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

- 从 GGUF 文件直接加载 tokenizer，零 C/C++ FFI、关键路径零 unsafe
- SPM/BPE/WPM/UGM/RWKV 全部与 llama.cpp 逐 token 验证一致
- 批量编码可选 Rayon，顺序后端结果确定性且可复现
- 支持 WASM/WASI 构建，41 种 BPE 预分词模式

## 适用场景

- 纯 Rust LLM 推理引擎中做分词，避免绑定 llama.cpp C++
- 浏览器 WASM 应用内运行 tokenization
- CLI 工具检查与调试 GGUF 模型的 tokenizer
- 嵌入式系统上无 C++ 工具链时进行分词

## 场景标签

 · 领域:LLM 基础设施/分词

## 证据(README 行号)

> L30: shimmytok is a **pure Rust tokenizer library** that reads tokenizers directly from GGUF model files. No Python, no 
> L39: **shimmytok extracts and runs the tokenizer directly from your GGUF file**, producing identical output to llama.cpp
> L156: - **LLM Inference Engines** — Pure Rust inference without C++ bindings

## 星数曲线

```mermaid
xychart-beta
    title "Michael-A-Kuykendall/shimmytok 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-29 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `fcd835a999cf` · [字段定义](../../DATASET.md)*
