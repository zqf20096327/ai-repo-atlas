# CX-ArtLab/BoopFace

⭐ 214 · JavaScript · MIT · 推送 2026-11-20 · [GitHub](https://github.com/CX-ArtLab/BoopFace) · [官网](https://boopface.com) · 个人维护

**为 AI 机器人和 Agent 提供表情化机器人头像 UI 组件**

基于 SVG 与原生 JavaScript 的 Web Component，零运行时依赖，MIT 许可；以 19 种动作（等待、成功、失败、愤怒、拒绝等）呈现 Agent 状态，支持指针跟随、拖拽形变、自动眨眼与睡眠策略，含 188 个纯 SVG 皮肤（17 个系列）与去掉皮肤的 lite 构建。另有 BoopFace Embedded：C++11 引擎把眼部表情运行到 ESP32/ESP32-S3/STM32/Raspberry Pi Pico 的 28 种板卡/屏幕配置固件，附在线模拟器与设置导出；嵌入式部分标注为实验性，尚未在实体硬件上验证。通过 npm 或 release zip 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 原生 Web Component，SVG 渲染，零运行时依赖，MIT 许可
- 19 种可编程 Agent 状态动作（等待/成功/失败/拒绝等）
- 188 个纯 SVG 皮肤（17 系列），lite 构建约 45 KB
- BoopFace Embedded 覆盖 28 种 ESP32/STM32/Pico 板卡与屏幕配置

## 适用场景

- 给聊天助手或编码 Agent 加一个显示等待/成功/失败状态的表情头像
- 为桌面伴侣、虚拟宠物、聊天机器人做视觉反馈层
- 在 ESP32/Pico 屏幕上跑同款机器人眼部表情固件

## 场景标签

 · 领域:前端 UI 组件/嵌入式

## 证据(README 行号)

> L13: BoopFace is a lightweight, expressive robot avatar component for AI bots, agents and interactive apps. Thinking, wa
> L15: Use it as the face and status feedback of AI assistants and agents: chat assistants like ChatGPT, Claude, Gemini, G
> L241: The Web avatar’s eye expressions now run on robot and development-board displays. The small C++11 engine preserves

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
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `416b160a2993` · [字段定义](../../DATASET.md)*
