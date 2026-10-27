# T8mars/comfyui-fireredaudio-T8

⭐ 24 · Python · Apache-2.0 · 推送 2026-09-30 · [GitHub](https://github.com/T8mars/comfyui-fireredaudio-T8) · [官网](https://huggingface.co/t8star/Firered-Audio-Comfy) · 个人维护 · 中文 README

**ComfyUI 的 FireRedAudio 全能力节点包：ASR、声音克隆与配音生产**

由 T8star-Aix 集成的 ComfyUI V3 节点包，封装 FireRedAudio 模型提供 45 个节点：多语言 ASR、长音频分段与 SRT/VTT 输出、中英文零样本声音克隆、语义语音编辑、批量配音与 QA 返修、多 Take 盲听评审、分轨交付 ZIP 等。通过独立 Worker 运行（Python 3.10/PyTorch 2.8 cu128/Transformers 5.8），不修改 ComfyUI 宿主环境；模型从 Hugging Face 固定 revision 下载，默认推荐 int8 量化变体。面向 ComfyUI 内容创作者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-24g` | |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 45 个节点覆盖 ASR、零样本声音克隆、语义编辑与批量配音生产
- 隔离 Worker 运行 Transformers 5.8，不污染 ComfyUI 宿主依赖
- 批配音含原子 manifest、断点恢复、ASR 回读 QA 与定向返修
- 模型下载固定 revision，支持 int8 量化与断点续传校验

## 适用场景

- 在 ComfyUI 中做有声书、播客、视频对白的批量配音与交付
- 零样本克隆音色并进行多 Seed 试音与盲听评审
- 长录音转写为 SRT/VTT 并做内容定位与证据片段导出

## 场景标签

`语音合成` `语音识别` · 领域:内容生成

## 证据(README 行号)

> L14: FireRedAudio 的 45 个 ComfyUI V3 全能力节点，由 **T8star-Aix** 集成。节点菜单：
> L20: - 多语言 ASR
> L24: - 中英文零样本声音克隆

## 星数曲线

```mermaid
xychart-beta
    title "T8mars/comfyui-fireredaudio-T8 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-27 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `796069f6dba4` · [字段定义](../../DATASET.md)*
