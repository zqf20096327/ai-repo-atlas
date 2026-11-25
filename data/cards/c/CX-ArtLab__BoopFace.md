# CX-ArtLab/BoopFace

⭐ 214 · JavaScript · MIT · 推送 2026-11-20 · [GitHub](https://github.com/CX-ArtLab/BoopFace) · [官网](https://boopface.com) · 个人维护 · 中文 README

**给 AI 助手/agent 用的表现力机器人头像 Web 组件与嵌入式眼睛引擎**

面向 AI 机器人、agent 与交互应用的表现力头像组件：原生 Web Component，SVG 渲染加原生 JavaScript，零运行时依赖，提供 188 个编号皮肤（17 系列）、等待/成功/失败等约 20 种表情动作、指针跟随与拖拽交互，供 ChatGPT、Claude Code、Cursor 等各类助手作为面孔与状态反馈层。另有 BoopFace Embedded（v0.1.0，实验性）：C++11 引擎在 ESP32、STM32、Raspberry Pi Pico 等 28 种板/屏配置上运行相同眼睛表情，含在线模拟器与固件示例；CI 编译全部配置但尚未在实体硬件验证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 原生 Web Component，SVG + vanilla JS，零运行时依赖
- 188 个编号皮肤（17 系列），lite 构建约 45 KB
- 可编程 agent 状态表情：waiting/success/failure/angry/love 等约 20 种动作
- BoopFace Embedded 支持 ESP32/STM32/Raspberry Pi Pico 共 28 种板/屏配置

## 适用场景

- 为聊天助手或编码 agent 添加可见的等待/成功/失败状态反馈
- 给桌面伴侣、虚拟宠物、聊天机器人做表情头像
- 在 ESP32/Pico 等开发板屏幕上驱动机器人眼睛表情

## 场景标签

 · 领域:前端组件/机器人人机界面

## 证据(README 行号)

> L13: BoopFace is a lightweight, expressive robot avatar component for AI bots, agents and interactive apps. Thinking, wa
> L15: Use it as the face and status feedback of AI assistants and agents: chat assistants like ChatGPT, Claude, Gemini, G
> L17: It also works for desktop companions, virtual pets, digital mascots, chatbot avatars and other interactive characte

## 星数曲线

```mermaid
xychart-beta
    title "CX-ArtLab/BoopFace 星数(近 15 点)"
    x-axis ["2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25"]
    y-axis "stars" 64 --> 227
    line [77, 83, 87, 88, 154, 162, 168, 178, 188, 199, 205, 208, 209, 210, 214]
```

2026-11-08 77 → 2026-11-25 214（+137）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-17 · 置信度 high · 依据 README sha `0eb7352cfa72` · [字段定义](../../DATASET.md)*
