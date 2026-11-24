# chenshiyi007/HttpRepeater

⭐ 5 · Go · Apache-2.0 · 推送 2026-11-09 · [GitHub](https://github.com/chenshiyi007/HttpRepeater) · 个人维护 · 中文 README

**安全测试者的桌面 HTTP 请求重放工具，含 AI 助手**

受 Burp Suite Repeater 启发的独立桌面 HTTP 重放工具：手写 TCP/TLS 套接字发送原始请求以保留头顺序与大小写，支持多标签、每标签代理链（Burp/Yakit/mitmproxy/Clash）、curl/fetch 导入、逐标签历史快照、响应解码与搜索。内置 AI 助手基于官方 OpenAI Go SDK v3，使用自有 LLM 端点改写请求或起草 payload，结果须人工确认后才发送。构建依赖 Go 1.26+、Node.js 20.19+ 与 Wails CLI v2.17+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 手写 TCP/TLS 发送保留原始请求头顺序、大小写与重复头
- curl/fetch 导入含 Chrome DevTools 的 bash 与 Windows cmd 两种格式
- 内置 AI 助手（自有 LLM 端点）改写请求/起草 payload，人工确认后才发送
- 每标签独立代理链、历史快照与会话内记忆

## 适用场景

- 从 DevTools 复制请求重放并调整参数验证漏洞报告
- 让 AI 助手把公告/CVE 描述转成可发送的验证请求
- 经 Burp/mitmproxy 代理链调试 HTTPS 目标
- 测试 Host 校验与 Content-Length 边界处理

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L12: A focused, standalone desktop HTTP request replay tool inspired by **Burp Suite Repeater**.
> L57: - **Optional AI help** — a built-in assistant backed by your own LLM endpoint can rewrite the
> L87: - **AI assistant** (bring your own LLM): chat about the current request, ask for edits or payloads,
> L89:  automatically. Built on the official **OpenAI Go SDK v3** with OpenAI-compatible **Chat

## 星数曲线

```mermaid
xychart-beta
    title "chenshiyi007/HttpRepeater 星数(近 3 点)"
    x-axis ["2026-10-30", "2026-10-31", "2026-11-24"]
    y-axis "stars" 3 --> 6
    line [4, 5, 5]
```

2026-10-30 4 → 2026-11-24 5（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 mid · 依据 README sha `04a13f21ae93` · [字段定义](../../DATASET.md)*
