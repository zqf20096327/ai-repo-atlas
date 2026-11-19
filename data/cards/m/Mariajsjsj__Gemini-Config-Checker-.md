# Mariajsjsj/Gemini-Config-Checker-

⭐ 62 · Go · Apache-2.0 · 推送 2026-11-18 · [GitHub](https://github.com/Mariajsjsj/Gemini-Config-Checker-) · 个人维护

**检测代理配置能否登录访问 Google AI Studio 与 Gemini 的工具**

以登录浏览器方式逐一测试代理配置能否实际进入 Google AI Studio 与 Gemini：先做连通性快筛淘汰失效配置，再用 Chrome/Edge/Brave 独立配置文件以用户账号读取 Google 的区域判定，并输出各产品可用状态、延迟与可导出的 Xray 配置。提供 Simple（检测自有配置）与 Advanced（将免费配置链接到基础配置之后换出口）两种模式，内置可编辑的反 DPI profile（Finalmask 分片、指纹、ALPN、加密套件）。提供 Windows/macOS/Linux 桌面包、Android APK 与可跨平台运行的 web server 构建；区域检查功能不支持 Android，仅连通模式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 登录浏览器读取 Google 区域判定，而非仅 HTTP 连通探测
- Simple/Advanced 双模式：检测自有配置或将免费配置链在基础配置之后
- 内置可编辑反 DPI profile（Finalmask fragment、指纹、ALPN、cipher）
- 每版本发布含 SHA256SUMS 校验文件

## 适用场景

- 使用前验证一组代理配置能否进入 AI Studio/Gemini
- Cloudflare 配置连通但被 Google 区域墙拦截时寻找其他出口
- 在受过滤网络中使用分片反 DPI 设置连接

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L11: Find proxy configs that actually get you into **Google AI Studio and Gemini**, by testing each one the way a person
> L14: > **Version 0.1.0, early pre-release.** It works end to end on Windows (the only platform it has been run on so far
> L50: Google decides region availability **per signed-in account, after the page has loaded**. A plain HTTP request (even

## 星数曲线

```mermaid
xychart-beta
    title "Mariajsjsj/Gemini-Config-Checker- 星数(近 2 点)"
    x-axis ["2026-11-18", "2026-11-19"]
    y-axis "stars" 61 --> 63
    line [62, 62]
```

2026-11-18 62 → 2026-11-19 62（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 mid · 依据 README sha `7119c240ac42` · [字段定义](../../DATASET.md)*
