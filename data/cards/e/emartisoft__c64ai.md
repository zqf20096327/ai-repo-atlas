# emartisoft/c64ai

⭐ 22 · C · MIT · 推送 2026-01-07 · [GitHub](https://github.com/emartisoft/c64ai) · 个人维护

**在 Commodore 64/128 上与 Gemini 聊天并同时播放 SID 音乐的应用**

C64AI 让 Commodore 64/128（或 VICE 模拟器）用户在真机上通过 User Port 串口与外部系统通信，接入 Gemini API 进行 AI 对话，同时持续播放 SID 音乐；界面支持 Commodore 1351 鼠标与键盘操作。外部系统可为 Raspberry Pi Zero 2（microSD 系统镜像、内置 Web 配置界面）或任意 64 位电脑，经 FT232RL USB-TTL 转换器或虚拟串口 + VICE 连接。服务端需配置 .env 中的 Gemini API key 与模型参数，c64aiserver 与 ask2ai 需分别用 GCC 和 Deno 构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- C64 与外部系统经 User Port + FT232RL 双向串口通信（2400 baud）
- 接入 Gemini API 的聊天，同时不中断 SID 音乐播放
- 支持 Commodore 1351 鼠标与键盘双操作方式
- 三种运行场景：VICE 模拟器、树莓派 Zero 2、任意 64 位电脑

## 适用场景

- 在真机 C64 上体验 AI 聊天并同时听 SID 音乐
- 无实体机时用 VICE + 虚拟串口运行测试
- 用树莓派 Zero 2 做嵌入式搭配的经典机联网方案

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L4: **C64AI** brings the spirit of modern artificial intelligence to the legendary **Commodore 64** — without sacrificin
> L71: To power up the AI core correctly, you **must configure the `.env` file** with your Gemini settings.

## 星数曲线

```mermaid
xychart-beta
    title "emartisoft/c64ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-30 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `2e8ac2176388` · [字段定义](../../DATASET.md)*
