# openai/birdingpal

⭐ 74 · Kotlin · MIT · 推送 2026-07-09 · [GitHub](https://github.com/openai/birdingpal) · 组织维护

**毛绒鸟类观察伴侣：ChatGPT 语音交互辅助识鸟与记录**

由 OpenAI 发布的观鸟随身伴侣项目：毛绒鸟外形的硬件（ESP32-S3 微控制器、压力传感器、蓝牙模块、麦克风与扬声器）配合移动应用，按下毛绒鸟即可启动语音会话，讨论所见所闻、录制鸟鸣并保存确认的观鸟记录到个人鸟书。语音体验使用 OpenAI Realtime API，可选接入 BirdNET 兼容端点分析 WAV 录音并返回候选鸟种。硬件为原型，含本地 Wi-Fi 调试面板。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按压毛绒鸟触发 ChatGPT 语音会话与鸟鸣录制
- 可选 BirdNET 兼容端点接收 WAV 音频与位置/周数元数据返回候选鸟种
- 确认后的观鸟记录保存至个人鸟书
- 固件内置本地 Wi-Fi 仪表盘用于调试与阈值调校

## 适用场景

- 户外观鸟时通过语音对话识别并记录鸟种
- 录制环境鸟鸣并获取候选鸟种分析
- 以实体毛绒伴侣形式携带使用，减少看屏幕

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L6: a custom Bluetooth controller and a ChatGPT-based voice interface so you can
> L46: analysis. The assistant can identify likely species, explain what it heard, and
> L51: optional BirdNET-compatible endpoint receives recorded WAV audio with location

## 星数曲线

```mermaid
xychart-beta
    title "openai/birdingpal 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-25"]
    y-axis "stars" 72 --> 75
    line [73, 74, 74]
```

2026-10-18 73 → 2026-10-25 74（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `b50db5750ad7` · [字段定义](../../DATASET.md)*
