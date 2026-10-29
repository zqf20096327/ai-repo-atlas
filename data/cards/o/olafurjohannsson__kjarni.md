# olafurjohannsson/kjarni

⭐ 38 · Rust · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/olafurjohannsson/kjarni) · [官网](https://kjarni.ai) · 个人维护

**本地推理引擎：在进程内做嵌入、语义搜索、分类、重排与文本生成**

用 Rust 从零实现的本地推理引擎，以单一共享库（.so/.dll/.dylib）形式随包分发，自带模型下载与缓存，首次下载后可离线运行。提供 C#、Go、Rust、Python、C++ 绑定、CLI 以及浏览器 WASM 包。功能覆盖嵌入、语义/关键词/混合检索、交叉编码器重排、情感与毒性分类、语音转文字、摘要与 seq2seq 指令生成；面向不希望搭建 Python 服务或使用托管 API、数据不能出本地的 .NET/Go 等应用开发者。GPU 路径走 WebGPU（Vulkan/DX12/Metal），输出经与 PyTorch 金标数值对齐的测试验证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单库进程内运行，无 PyTorch/ONNX Runtime 等运行时依赖
- 内置索引与 BM25+向量混合检索，无需单独向量数据库
- 多语言绑定（C#/Go/Rust/Python/C++）、CLI 与浏览器 WASM 版
- 支持约 17 个 HuggingFace 模型，覆盖嵌入、重排、分类、Whisper 转录、摘要与 flan-t5 生成

## 适用场景

- 在 .NET/Go 应用中直接加语义搜索或文本分类，不依赖 Python 服务
- 数据敏感场景（法律/医疗/金融）下完全本地运行嵌入与分类
- 在浏览器页面内做本地语义排序与对话推理

## 场景标签

`推理引擎` `语义搜索` `语音识别` · 领域:知识与检索

## 证据(README 行号)

> L12: Kjarni is a native inference engine written from scratch in Rust. It ships as a single shared library, downloads it
> L10: **Local embeddings, semantic search, classification, reranking and chat for C#, Go, Rust, Python, C++ and the comma

## 星数曲线

```mermaid
xychart-beta
    title "olafurjohannsson/kjarni 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-29"]
    y-axis "stars" 36 --> 39
    line [37, 38, 38]
```

2026-10-18 37 → 2026-10-29 38（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `1cdc30154f49` · [字段定义](../../DATASET.md)*
