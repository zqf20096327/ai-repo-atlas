# charleszhang309/Vitals

⭐ 4 · Python · MIT · 推送 2026-11-27 · [GitHub](https://github.com/charleszhang309/Vitals) · 个人维护 · 中文 README

**本地优先的个人状态面板与跨设备控制中心，带可选 AI 助手**

以 FastAPI + React/Tauri 构建的本地个人状态中枢：提供可定制 Bento 今日面板、Windows/macOS 硬件监控与远程控制、iPad/iPhone 无线 Deck 与插件商店、全屏歌词播放器、跨设备草稿板，以及可选 AI 助手（通过 config.json 配置 api_key 与模型）。单机使用打开本地端口即可；多设备访问推荐先配置 Tailscale 并由设置向导一键生成 HTTPS 地址与配对令牌。数据本地优先，无云端锁定。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 可定制 Bento 今日面板：天气、健康环、双向日历、汇率、专注时钟等组件
- Windows（LibreHardwareMonitor/psutil）与 macOS 原生传感器读取，支持 Smart/Live/Eco 三档采样
- iPad/iPhone 无线 Deck 触控台，内置插件商店与声明式插件 SDK（官方 OBS、DaVinci Resolve 插件）
- 可选 AI 助手，通过 backend/agent.md 热重载自定义助手人格

## 适用场景

- 在桌面与 iPad 之间搭建无线触控控制台远程操控电脑
- 聚合 Apple 健康/Health Connect 数据到统一的今日面板
- 跨 Windows 与 MacBook 切换控制硬件状态与媒体播放

## 场景标签

 · 领域:效率/个人状态面板

## 证据(README 行号)

> L7: Unifies a customizable **Today Bento Dashboard**, real-time **Windows & macOS Hardware Monitoring & Remote Control**
> L70: - `ai`: `enabled`, `api_key`, `model`. Edit `backend/agent.md` to customize assistant persona with hot reload.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `d4e1ee539b5e` · [字段定义](../../DATASET.md)*
