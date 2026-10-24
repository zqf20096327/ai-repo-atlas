# microsoft/ai-audio-descriptions

⭐ 54 · Python · MIT · 推送 2026-09-07 · [GitHub](https://github.com/microsoft/ai-audio-descriptions) · 组织维护

**用 AI 为视频生成可编辑的音频描述（无障碍旁白）草稿**

端到端的音频描述制作工作流：GenerateAD 分析 MP4，识别对白间的旁白窗口，生成 WebVTT 草稿；人工编辑审校后由 RenderAD 用语音合成渲染出带描述的新视频（自动压低原声并混音）。另含 SeparateAD（从已有 AD 混音中分离旁白轨）和浏览器端 Studio 编辑器。依赖 Python、Node.js 20.19+、FFmpeg、Azure 订阅与 Microsoft Foundry（Speech + GPT 部署）。本地单进程运行，不提供认证、多服务器协调或共享云存储。

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

- GenerateAD 从 MP4 识别旁白窗口并生成 WebVTT 描述草稿
- RenderAD 合成语音、适配旁白窗口、压低原声并混音输出 MP4
- SeparateAD 从匹配的主音轨与 AD 音轨恢复近似纯旁白 WAV
- 浏览器端 Studio 提供上传、进度、同步字幕预览与下载，数据存于本地 data/ 目录

## 适用场景

- 为盲人或低视力观众快速制作视频音频描述轨
- 音频描述编辑审校 AI 生成的草稿后渲染成品
- 从已有广播级 AD 混音中提取旁白轨

## 场景标签

`语音合成` `图像视频处理` · 领域:内容生成

## 证据(README 行号)

> L10: This project uses artificial intelligence to assist with creating an audio
> L11: description track. It analyzes an MP4, identifies narration windows, and generates
> L42: GenerateAD converts an MP4 into a WebVTT draft. Each cue covers an available

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/ai-audio-descriptions 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-23", "2026-10-24"]
    y-axis "stars" 51 --> 55
    line [52, 53, 54, 54]
```

2026-10-18 52 → 2026-10-24 54（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `a0e831b754e8` · [字段定义](../../DATASET.md)*
