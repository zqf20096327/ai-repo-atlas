# religa/halloween-candy-dispenser

⭐ 3 · Python · Apache-2.0 · 推送 2026-11-01 · [GitHub](https://github.com/religa/halloween-candy-dispenser) · [官网](https://www.youtube.com/watch?v=f7yGwlmqU8s) · 个人维护

**给万圣节讨糖场景做一台可 3D 打印的会说话 AI 糖果机**

一个完整的 DIY 项目：装在 5 加仑桶里的自动糖果分发器与 6 英尺女巫道具。声纳检测到访客后，语音程序经 ElevenLabs 做语音转文本、Claude 按人设对话、ElevenLabs 合成回复；说出"trick or treat"由代码（非模型）执行发糖限额与冷却。硬件侧 Arduino Uno 经 TB6600 驱动 NEMA 23 步进电机转盘，红外对射确认落糖。所有打印件由 build123d 参数化 Python 脚本生成，含几何测试，适配 Bambu A1 mini 打印板。Apache 2.0 许可，需 Anthropic 与 ElevenLabs API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Claude 对话 + ElevenLabs 语音转写与合成的对话女巫
- 发糖限额、冷却由代码强制而非模型控制
- 全部打印件为 build123d 参数化脚本并带几何测试
- systemd 服务含重连、看门狗与离线兜底台词

## 适用场景

- 万圣节在家门口搭一台会对话并自动发糖的道具
- 学习 LLM 语音对话与 Arduino 硬件的结合开发
- 用参数化 CAD 脚本定制修改打印件尺寸

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L3: **A talking, AI-powered Halloween candy dispenser you can 3D print.**
> L22: An automatic Halloween candy dispenser in a 5-gallon bucket, with a 6 ft witch prop that talks
> L190: **Can I run the dispenser without the witch?** For testing, yes: `uv run tools/dispense.py`

## 星数曲线

```mermaid
xychart-beta
    title "religa/halloween-candy-dispenser 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-11-23"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-10-26 3 → 2026-11-23 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `ca9c3798f52a` · [字段定义](../../DATASET.md)*
