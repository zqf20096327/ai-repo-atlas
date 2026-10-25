# Aegis-plus/SillyTavern-Android

⭐ 54 · Java · ISC · 推送 2026-02-03 · [GitHub](https://github.com/Aegis-plus/SillyTavern-Android) · 个人维护

**自托管 SillyTavern 的 Android WebView 启动器**

基于 Capacitor 构建的 Android 应用，通过全屏 WebView 访问用户自托管的 SillyTavern 实例：移除浏览器 UI，提供文件上传、相机与麦克风的原生权限支持，可保存实例 URL 一键连接。使用方式为下载 Releases 页面的预构建 APK 安装；也可通过 GitHub Actions 或本地环境（Node.js >=22、Android Studio、JDK 21）自行构建签名 APK。本体是 SillyTavern 的访问客户端，需用户自行部署服务端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | ISC |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 全屏 WebView 访问自托管 SillyTavern 实例
- 文件上传、相机与麦克风的原生权限支持
- 提供预构建 APK，支持 GitHub Actions 自动构建签名包

## 适用场景

- 在 Android 设备上以应用形式访问自己的 SillyTavern
- 多模态聊天时直接调用手机相机与麦克风
- 不想用完整浏览器、追求轻量访问方式

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: A lightweight Android wrapper for SillyTavern. This application provides a dedicated WebView environment to access y
> L28:  - Enter the full URL of your SillyTavern instance (e.g., `http://192.168.1.5:8000` or your public tunnel URL).

## 星数曲线

```mermaid
xychart-beta
    title "Aegis-plus/SillyTavern-Android 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-25"]
    y-axis "stars" 52 --> 55
    line [53, 54, 54]
```

2026-10-18 53 → 2026-10-25 54（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `023acaca74c9` · [字段定义](../../DATASET.md)*
