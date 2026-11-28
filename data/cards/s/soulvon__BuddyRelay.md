# soulvon/BuddyRelay

⭐ 3 · TypeScript · MIT · 推送 2026-11-27 · [GitHub](https://github.com/soulvon/BuddyRelay) · [官网](https://open-vsx.org/extension/soulvon/buddy-relay) · 个人维护 · 中文 README

**CodeBuddy IDE 多账号管理与无感切号扩展**

一款以 .vsix 形式发布的扩展，仅运行于电脑桌面端 CodeBuddy IDE（国内版/国际版）。通过进程级会话更新与跨账号目录软链接映射，实现切号不关窗口、不重启编辑器、历史会话互通；提供多账号卡片流、算力余额直读与用量分析、额度见底或 429 限流时自动切号、一键签到与成长任务自动化、Cockpit Tools/JSON/OAuth 多源账号导入。凭据以 AES-256-GCM 本地加密落盘；Windows/macOS/Linux 支持。WorkBuddy 各端与 CLI 无扩展系统，不能安装本插件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 进程级无感切号：不关窗口、不重启、历史会话软链接互通
- 额度实时监控与阈值/429 触发的自动切号（含探针预检与频率熔断）
- 一键签到与成长任务自动化（定时调度、随机抖动）
- 纯本地运行：凭据 AES-256-GCM 加密落盘，无遥测

## 适用场景

- 在 CodeBuddy IDE 中维护多个账号，额度耗尽自动切换不中断编码
- 定时自动签到与完成平台成长任务，积分各端共享
- 直播/录屏时对账号名称、邮箱与 UID 一键脱敏
- 多窗口场景下同步号池并防止双窗口抢号

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L32: BuddyRelay 是一款专为**电脑桌面端 CodeBuddy IDE**（国内版 CodeBuddy CN / 国际版 CodeBuddy）打造的多账号管理与无感切号扩展（`.vsix`）。通过进程级会话更新与跨账号目录软链
> L35: > 1. **唯一运行宿主**：本扩展**必须且只能运行在电脑桌面端的 CodeBuddy IDE 编辑器中**（Windows / macOS / Linux）。WorkBuddy 桌面客户端、WorkBuddy 手机 App、
> L148: |**BuddyRelay 插件安装宿主 (.vsix)**|✅ 原生完整支持|✅ 原生完整支持|❌ 独立软件，无扩展系统|❌ 独立软件，无扩展系统|


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `453d50fc5df4` · [字段定义](../../DATASET.md)*
