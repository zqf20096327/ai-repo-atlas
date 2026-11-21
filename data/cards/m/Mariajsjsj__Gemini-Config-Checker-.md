# Mariajsjsj/Gemini-Config-Checker-

⭐ — · [GitHub]() · 个人维护

**检测代理配置能否访问 Google AI Studio 与 Gemini 的桌面工具**

以登录浏览器方式逐个测试代理配置：通过用户自己的 signed-in 浏览器访问 AI Studio/Gemini，读取 Google 对该出口的区域判定，避免普通连通性探测的假阳性。提供 Simple（检测手头配置哪些可用）与 Advanced（在可用基础配置后链式接免费配置以换出口）两种模式，内置 anti-DPI 片段化配置（面向伊朗等过滤网络），支持 vless/vmess/trojan/ss 链接、订阅 URL 与 base64 输入，可导出链接/base64/Xray 配置。应用内嵌 Xray-core 作为代理引擎，基于 Wails 桌面壳，提供 Windows/macOS/Linux/Android 构建与 Web 服务器模式；v0.1.0 早期预发布版，仅 Windows 实测过。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 登录浏览器区域检测：读取 Google 对 signed-in 账号的真实区域判定
- Simple/Advanced 双模式，Advanced 可将免费配置链在可用基础配置后
- 可编辑的 anti-DPI 配置（Finalmask fragment、指纹、ALPN、cipher）
- 导出链接、base64 或链式 Xray 配置

## 适用场景

- 使用前先验证某个代理配置能否进入 AI Studio/Gemini
- 批量筛选手头配置中哪些出口未被 Google 区域封锁
- 在 DPI 过滤网络下用 anti-DPI 配置完成检测

## 场景标签

 · 领域:网络工具/代理配置检测

## 证据(README 行号)

> L11: Find proxy configs that actually get you into **Google AI Studio and Gemini**, by testing each one the way a person
> L50: Google decides region availability **per signed-in account, after the page has loaded**. A plain HTTP request (even
> L43: |XTLS/Xray-core|The proxy engine embedded in the app|

## 星数曲线

```mermaid
xychart-beta
    title "Mariajsjsj/Gemini-Config-Checker- 星数(近 2 点)"
    x-axis ["2026-11-18", "2026-11-20"]
    y-axis "stars" 56 --> 63
    line [62, 57]
```

2026-11-18 62 → 2026-11-20 57（-5）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `ce08b89e3a30` · [字段定义](../../DATASET.md)*
