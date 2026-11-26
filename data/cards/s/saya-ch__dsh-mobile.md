# saya-ch/dsh-mobile

⭐ 1,005 · TypeScript · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/saya-ch/dsh-mobile) · 个人维护 · 中文 README

**在手机上安全访问电脑中 DeepSeek Harness 的移动端插件与 Android App**

DSH Mobile 是 DeepSeek Harness 的社区插件，让手机浏览器或 Android App 通过局域网或多种远程通道（Tailscale Funnel、cpolar、cloudflared、自建 FRP、反向代理、实验性 iroh）连接电脑，延续使用电脑端的会话、工作区、消息和工具。提供触屏布局适配、扫码/链接配对与设备管理、独立 HTTPS 与证书信任机制、iPhone/iPad 主屏幕 Web App 与网页推送、任务通知、诊断报告，以及通过 /mobile 命令在对话中定制手机端。插件不修改 DeepSeek Harness 源码；远程访问默认关闭，iroh 为实验性功能，Windows 客户端为 alpha 预览。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 局域网与多种远程通道连接，含无需域名的实验性 iroh 加密直连
- 扫码/链接配对、设备列表管理与一键撤销授权
- iPhone/iPad 主屏幕 Web App（PWA）与网页推送（六类提醒）
- 在 DSH 对话中用 /mobile 命令定制手机端界面

## 适用场景

- 在手机上继续使用电脑中 DeepSeek Harness 的会话与工具
- 离开电脑所在网络时通过远程隧道访问 DSH
- iPhone/iPad 添加到主屏幕接收任务完成提醒
- 鸿蒙等无法安装 APK 的设备用浏览器配对访问

## 场景标签

 · 领域:开发工具/移动端远程访问

## 证据(README 行号)

> L1: 用手机使用电脑中的 DeepSeek Harness
> L51: DSH Mobile 是一个 DeepSeek Harness 插件，让手机浏览器或 Android App 通过局域网，或可选的 Tailscale Funnel、cpolar、cloudflared、自建 FRP、自有反向代理


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `6bdd26ce0111` · [字段定义](../../DATASET.md)*
