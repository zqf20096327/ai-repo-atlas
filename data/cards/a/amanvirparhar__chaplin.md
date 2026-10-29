# amanvirparhar/chaplin

⭐ 759 · Python · MIT · 推送 2025-11-02 · [GitHub](https://github.com/amanvirparhar/chaplin) · 个人维护

**实时唇读工具：读取唇部动作并打出无声语音文本**

视觉语音识别（VSR）桌面工具：通过摄像头捕捉用户无声口型的唇部动作，基于 LRS3 数据集训练的 Auto-AVSR 模型识别出文本，全部本地运行。识别的原始输出记录在终端，再由本地 LLM（通过 Ollama 拉取 qwen3:4b）修正后自动输入到光标处。安装方式为克隆仓库后运行 setup.sh 自动下载 Hugging Face 模型，使用 uv 与 Python 3.12 运行，按 option/alt 键启停录制，Mac/Windows/Linux 均有对应按键。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 Auto-AVSR/LRS3 模型的实时唇读识别
- 全本地运行，无需云端服务
- LLM 修正后的文本自动输入到光标位置
- setup.sh 自动从 Hugging Face Hub 下载模型文件

## 适用场景

- 无法发声或需保持安静的环境下用口型输入文字
- 为不便打字的场景提供无声语音输入
- 本地运行唇读识别进行实验或演示

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L5: A visual speech recognition (VSR) tool that reads your lips in real-time and types whatever you silently mouth. Runs
> L7: Relies on a model trained on the Lip Reading Sentences 3 dataset as part of the Auto-AVSR project.

## 星数曲线

```mermaid
xychart-beta
    title "amanvirparhar/chaplin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 758 --> 760
    line [759, 759]
```

2026-10-18 759 → 2026-10-29 759（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `34f6464733c9` · [字段定义](../../DATASET.md)*
