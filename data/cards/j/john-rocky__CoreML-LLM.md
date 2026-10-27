# john-rocky/CoreML-LLM

⭐ 201 · Python · MIT · 推送 2026-10-05 · [GitHub](https://github.com/john-rocky/CoreML-LLM) · [官网](https://john-rocky.github.io/) · 个人维护

**在 Apple 神经引擎上本地运行 LLM 的 Swift 包**

面向 iOS 18+/macOS 15+ 的 Swift Package，通过 Core ML 在 Apple Neural Engine（ANE）上运行 Gemma 4、Qwen3.5、Qwen3-VL、LFM2.5 等模型，支持文本、多模态、流式输出、多轮对话、函数调用（FunctionGemma）与句向量（EmbeddingGemma）；首次调用从 HuggingFace 路径下载模型并复用本地包。README 给出持续解码对比数据（ANE 相比 GPU 运行时保留更多吞吐），并提供模型转换流程文档与 Python 转换环境要求。App Store 提供 Models Zoo 预构建应用，也可从 Xcode 工程构建。

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

- ANE-first 推理，计算单元默认 .cpuAndNeuralEngine
- 支持 13 个已转换模型，含多模态、函数调用与嵌入模型
- 后台 URLSession 下载，支持暂停/恢复
- 提供自有模型转换流程（coremltools 8+、PyTorch 2.2+）

## 适用场景

- 在 iPhone 应用中本地运行 LLM 聊天而不占用 GPU
- 在 iOS/macOS 应用中做设备端函数调用与 RAG 嵌入
- 将自有 HuggingFace 模型转换为 Core ML 并在 ANE 上部署

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L5: Where MLX Swift is the right call when you want maximum GPU throughput, CoreML-LLM is what you use when the LLM shou
> L27: let llm = try await CoreMLLLM.load(repo: "lfm2.5-350m")
> L104: Set your development team → build to an iOS 18+ device → **Get Model** → download → chat. Compute units default to

## 星数曲线

```mermaid
xychart-beta
    title "john-rocky/CoreML-LLM 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-27"]
    y-axis "stars" 199 --> 202
    line [200, 201, 201]
```

2026-10-18 200 → 2026-10-27 201（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `e6f9c5a2ad6c` · [字段定义](../../DATASET.md)*
