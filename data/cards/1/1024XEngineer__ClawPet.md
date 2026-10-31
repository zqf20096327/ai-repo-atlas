# 1024XEngineer/ClawPet

⭐ 14 · Go · MIT · 推送 2026-05-13 · [GitHub](https://github.com/1024XEngineer/ClawPet) · 组织维护 · 中文 README

**基于 LLM 的桌面陪伴宠物，提供情绪理解与轻任务辅助**

Electron + Next.js 前端与 Go 后端（launcher/gateway）组成的三段式桌宠应用：桌宠窗口渲染于 /desktop-pet 页面，默认出现在主屏幕右下角。README 为开发说明，描述一键 PowerShell 启动脚本与前后端分别启动方式；无本地二进制时脚本回退 go run 启动后端，需系统预装 Go 与 Node.js。产品定位为工作学习时的陪伴与随口记录、主动提醒等轻任务辅助，但 README 可见范围内未展示情绪理解等能力的实现细节。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- launcher/gateway/前端三段启动链路，端口可通过脚本参数覆盖
- 一键 PowerShell 脚本启动，缺二进制时回退 go run
- Electron 桌宠壳层 + Next.js 面板的前端结构

## 适用场景

- 在桌面常驻一只提供陪伴的桌宠
- 工作学习时获得随口记录与主动提醒等轻任务辅助
- 开发者本地启动并排查桌宠渲染与端口问题

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L16: - `clawpet-frontend/clawpet`：Next.js 面板 + Electron 桌宠壳层
> L22: powershell -ExecutionPolicy Bypass -File .\scripts\run-goclaw-dev.ps1 -Restart -PetclawMode dev

## 星数曲线

```mermaid
xychart-beta
    title "1024XEngineer/ClawPet 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `10d9fbfe5fbd` · [字段定义](../../DATASET.md)*
