# bentoml/BentoWhisperX

⭐ 18 · Python · 推送 2026-07-14 · [GitHub](https://github.com/bentoml/BentoWhisperX) · 组织维护

**用 BentoML 部署 WhisperX 语音识别推理 API 的示例工程**

BentoML 官方示例项目：将 WhisperX（带词级时间戳与说话人分离的自动语音识别）封装为 BentoML Service，通过 bentoml serve 启动 HTTP 推理服务，提供 /transcribe 接口，可用 curl 或 Python 客户端上传音频文件转录。说话人分离依赖 pyannote 模型，需向 Hugging Face 申请访问并提供 HF_TOKEN。支持部署到 BentoCloud，或用 BentoML 生成 OCI 镜像自托管。面向想在生产环境运行语音识别 API 的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 将 WhisperX 封装为 BentoML Service 的 HTTP 推理 API
- 支持词级时间戳与说话人分离（需 pyannote 模型访问授权与 HF_TOKEN）
- 可一键部署到 BentoCloud 或生成 OCI 兼容镜像自托管

## 适用场景

- 快速搭建本地语音转写 HTTP 服务用于测试
- 将语音识别 API 部署到 BentoCloud 统一管理
- 作为编写 BentoML 语音推理服务的参考模板

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L3: WhisperX provides fast automatic speech recognition with word-level timestamps and speaker diarization.
> L5: This is a BentoML example project, demonstrating how to build a speech recognition inference API server, using the W

## 星数曲线

```mermaid
xychart-beta
    title "bentoml/BentoWhisperX 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-29 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `a201f8c207e9` · [字段定义](../../DATASET.md)*
