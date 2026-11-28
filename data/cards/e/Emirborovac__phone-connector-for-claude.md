# Emirborovac/phone-connector-for-claude

⭐ 94 · Python · MIT · 推送 2026-11-27 · [GitHub](https://github.com/Emirborovac/phone-connector-for-claude) · 个人维护

**让 Claude Code 控制安卓手机/模拟器的插件，代管应用操作**

一个 Claude Code 插件：一条命令在电脑上创建带 Play Store 的 Android 模拟器（或经 USB/Wi-Fi 连接真实安卓机），Claude 通过 ADB 点按、输入、滚动并读取屏幕文本与截图来操作应用，首次使用时记录各应用的界面笔记。内置发送前确认、批量操作限速、永不接触密码等安全规则，数据留存本地。也提供独立的 PowerShell/Python 脚本供终端直接使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一键创建带 Play Store 的桌面 Android 模拟器（约 3 GB 下载）
- 通过官方 ADB 操作手机，无 root、无 hack
- 支持连接真实安卓手机（USB 或 Wi-Fi 配对引导）
- 发送前强制确认、批量操作限速、本地存储隐私规则

## 适用场景

- 让 Claude 汇总收件箱并代拟邮件回复
- 代看 LinkedIn/X/YouTube 的私信、评论并起草回复
- 在电脑上用 Claude 操作任意已安装的安卓应用

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L8:  Claude Code plugin
> L66: - It taps, types and scrolls through **ADB**, Android's own developer connection. No hacks and no root.
> L71: You need Claude Code and Python 3.8+ (already on most Macs and Linux machines; on Windows get it from python.org or


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `973ac41eee8a` · [字段定义](../../DATASET.md)*
