# kroko-ai/kroko-onnx

⭐ 162 · C++ · Apache-2.0 · 推送 2026-05-28 · [GitHub](https://github.com/kroko-ai/kroko-onnx) · [官网](https://kroko.ai) · 组织维护

**开源语音识别引擎：流式语音转文字，多平台部署**

Kroko ASR 的开源语音转文字引擎，基于 ONNX Runtime 运行转导模型，提供流式 WebSocket 转写服务（final/partial/segment/word 四级 JSON 输出）与 Python 包（OnlineRecognizer）。模型分 CC-BY-SA 社区版与需许可证密钥的商业版两种；商业版构建需开启 KROKO_LICENSE 并链接 OpenSSL。支持 CPU/CUDA/CoreML 执行后端、端点检测与 beam search 解码。构建产物覆盖 Linux、Docker、macOS wheel、Windows NSIS 安装包与 wheel，另有 Android 原生与浏览器 WASM 演示。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 流式 WebSocket 转写服务器（默认端口 6006），输出 final/partial/segment/word 级 JSON
- Python 包 OnlineRecognizer，支持 cpu/cuda/coreml 执行后端与端点检测
- 社区模型 CC-BY-SA 许可，商业模型需许可证密钥
- 提供 Android 原生与浏览器 WASM 演示

## 适用场景

- 搭建流式语音转文字服务，实时获取转写结果
- 在 Python 中离线转写 wav 音频文件
- 在手机端或浏览器内运行本地语音识别

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L1: ## **Open-source speech recognition built for developers.**
> L3: > Our engine is fully open-source, and you choose how to deploy models: use our **CC-BY-SA licensed community models
> L246: recognizer = kroko_onnx.OnlineRecognizer.from_transducer(

## 星数曲线

```mermaid
xychart-beta
    title "kroko-ai/kroko-onnx 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 161 --> 163
    line [162, 162]
```

2026-10-18 162 → 2026-10-23 162（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `101a66f7c819` · [字段定义](../../DATASET.md)*
