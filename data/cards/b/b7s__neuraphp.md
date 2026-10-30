# b7s/neuraphp

⭐ 15 · PHP · 推送 2026-06-05 · [GitHub](https://github.com/b7s/neuraphp) · [官网](https://brunots.dev/) · 个人维护

**给 PHP 开发者的本地文本 embedding 库：无 API、无外部服务**

通过 PHP FFI 直接调用 C 库（embedding.cpp 编译出的 libbert_shared.so）在本机生成文本 embedding，无网络调用。支持 AllMiniLM、BGE、E5、多语言等 BERT 兼容 HuggingFace 模型，提供 F32/F16/Q4 量化与余弦相似度等向量运算。CLI 工具 neuraphp install 可自动克隆、编译依赖并下载转换 GGUF 模型；需 PHP 8.3+，编译库需 CMake、C++ 编译器、Rust 等工具链。提供可选 Laravel 集成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PHP FFI 直连 C 库生成 embedding，无需 API 与外部服务
- 支持多种 BERT 兼容 HuggingFace 模型与 F32/F16/Q4 量化
- CLI 自动完成依赖编译与 GGUF 模型下载转换
- 提供余弦相似度、点积、欧氏距离等向量运算与可选 Laravel 集成

## 适用场景

- PHP/Laravel 应用内本地生成文本 embedding
- 构建不依赖外部 API 的语义搜索或相似度计算
- 数据不出服务器的隐私敏感 embedding 场景

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L5: NeuraPHP brings local AI embeddings to PHP—no APIs, no subscriptions, no external services. Run fast, private, perso
> L13: - **PHP FFI** — Direct memory access to a **C library**, no separate process

## 星数曲线

```mermaid
xychart-beta
    title "b7s/neuraphp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `dd2ef4fc7d37` · [字段定义](../../DATASET.md)*
