# AnshSinglaDev/Akshar-hindi-hinglish

⭐ 3 · C++ · NOASSERTION · 推送 2026-10-17 · [GitHub](https://github.com/AnshSinglaDev/Akshar-hindi-hinglish) · 个人维护

**给需要印地文转 Hinglish 的开发者提供离线低延迟音译引擎**

用 C++17 编写的印地文（天城文）到 Hinglish（罗马字）神经音译运行时，基于 ByT5 模型，通过 Vulkan GPU 或 AVX2 CPU SIMD 运行，本地离线执行。Windows 提供预编译可执行文件（约 19 MB），模型权重托管在 Hugging Face（GGUF/ONNX/CTranslate2/PyTorch 四种格式）。应用以 stdin/stdout 管道方式集成到 Python、Node.js、C++ 等宿主程序，支持批处理文件转换、hotwords 个性化、长度钳制与重复 ngram 抑制等护栏选项。许可为 CC BY-NC 4.0，禁止商业收费使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地离线运行，单句音译约 10–15ms（README 自测数据）
- GGUF/ONNX/CTranslate2/PyTorch 四种模型格式可选
- stdin/stdout 管道集成，无需 Python/PyTorch/CUDA 依赖
- 内置 auto-terminate、length-ratio、no-repeat-ngram 等解码护栏与 hotwords 覆写

## 适用场景

- 为印地语直播/视频字幕流程生成 Hinglish 罗马字文本
- 在自己的 Python/Node.js 应用中以子进程方式调用音译
- 批量转换印地文文本文件为 Hinglish
- 无显卡服务器上用纯 CPU 模式跑 ONNX 推理

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L10:  Akshar Engine (Hindi to Hinglish) converts Hindi (Devanagari script) into natural, everyday Hinglish (Roman Englis
> L12:  Runs 100% offline on your own machine in ~10 to 15 milliseconds per sentence — no internet or cloud API required.
> L107: If you are building your own application, subtitle tool, bot, or web backend, you don't need complex C++ bindings 

## 星数曲线

```mermaid
xychart-beta
    title "AnshSinglaDev/Akshar-hindi-hinglish 星数(近 2 点)"
    x-axis ["2026-10-21", "2026-11-23"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-10-21 3 → 2026-11-23 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `11860bb35d9e` · [字段定义](../../DATASET.md)*
