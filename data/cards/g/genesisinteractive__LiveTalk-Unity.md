# genesisinteractive/LiveTalk-Unity

⭐ 53 · C# · MIT · 推送 2026-10-25 · [GitHub](https://github.com/genesisinteractive/LiveTalk-Unity) · 组织维护

**Unity 端侧数字人库：输入肖像与文本生成本地语音与口型视频**

面向 Unity 开发者的说话头像生成包，组合 LivePortrait、MuseTalk 与 Qwen3-TTS 三个模型：LivePortrait 为静态肖像生成表情与头部动作，MuseTalk 实时唇形对齐，Qwen3-TTS 支持按描述设计声音或从录音克隆声音。PyTorch 模型已导出为 ONNX 并针对 CoreML 优化，通过 ONNX Runtime 在本地推理，macOS 用 CoreML，Windows 可用 CUDA/WebGPU，否则 CPU。模型权重需自行下载（Qwen3 检查点各约 8GB）。以 Unity Package 形式经 git URL 或 OpenUPM 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三模型统一 API：LivePortrait 表情驱动 + MuseTalk 实时唇形同步 + Qwen3-TTS 设计/克隆声音
- 全部本地推理：ONNX 导出并针对 CoreML 优化，Windows 支持 CUDA/WebGPU 回退 CPU
- Avatar/Voice/Character 三实体独立生命周期，基于内容哈希的 get-or-create 与缓存
- 语音按 voice+text、口型帧按 voice+text+avatar+expression 缓存

## 适用场景

- 在 Unity 游戏或应用中生成可对话的本地数字人角色
- 从一张肖像和一行文本直接产出带语音的口型视频流
- 用文本描述设计新声音或从 4 秒以上录音克隆声音

## 场景标签

`语音合成` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L3: On-device talking-head characters for Unity. Give it a portrait and a line of
> L15: The PyTorch models of the first two were exported to ONNX and tuned for CoreML;
> L100: Download the pre-exported ONNX models from

## 星数曲线

```mermaid
xychart-beta
    title "genesisinteractive/LiveTalk-Unity 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 52 --> 54
    line [53, 53]
```

2026-10-18 53 → 2026-10-25 53（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `cb6b25108f60` · [字段定义](../../DATASET.md)*
