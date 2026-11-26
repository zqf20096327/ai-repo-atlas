# daniloofrs/speech-to-prompt-pipeline

⭐ 3 · Python · MIT · 推送 2026-11-07 · [GitHub](https://github.com/daniloofrs/speech-to-prompt-pipeline) · 个人维护

**本地语音转结构化提示词的桌面工具：按 F8 说话即注入光标**

面向 Windows 桌面的语音输入工具：按 F8 开始说话，经 Faster-Whisper 转录后由本地 LLM（llama-cpp-python 进程内运行 Qwen 2.5 1.5B GGUF）按 4 种预设（code/commit/english/clean）合成提示词，并通过 Win32 句柄向当前光标注入 Ctrl+V。全部推理在本地 GPU VRAM 完成，宣称无云端传输。附带 PostgreSQL 16 的批量摄取与审计批次（Docker 部署）、网页监控仪表盘及 38 个单元测试。MIT 许可，Python 3.12+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Faster-Whisper 转录 + 进程内 Qwen2.5 GGUF 生成，全程本地 GPU 推理
- Win32 句柄捕获与自动 Ctrl+V 注入到当前编辑器光标
- 4 种可切换的提示词预设，其中 clean 模式绕过 LLM 直接输出转录
- VAD 静音自动结束录制（3 秒）与程序化音效反馈

## 适用场景

- 写代码时用语音生成结构化提示词并直接粘贴到编辑器
- 口述改动内容自动生成 Conventional Commits 提交信息
- 批量记录语音条目到 PostgreSQL 做数据工程与审计

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L7: > Transforme comandos de voz informais em prompts estruturados de alta densidade em menos de 300ms diretamente no cu
> L21: - **⚡ Latência Instantânea (< 300ms):** Substituição de gargalos HTTP REST por um motor LLM in-process na GPU (`lla
> L117: |`LLM_BACKEND`|`embedded`|Motor do LLM: `embedded` (GGUF in-process na GPU), `direct` (Whisper puro) ou `ollama` (

## 星数曲线

```mermaid
xychart-beta
    title "daniloofrs/speech-to-prompt-pipeline 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-26"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-08 3 → 2026-11-26 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 mid · 依据 README sha `95e98e24bb54` · [字段定义](../../DATASET.md)*
