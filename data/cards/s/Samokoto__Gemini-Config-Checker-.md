# Samokoto/Gemini-Config-Checker-

⭐ 62 · Go · Apache-2.0 · 推送 2026-11-18 · [GitHub](https://github.com/Samokoto/Gemini-Config-Checker-) · 个人维护

**检测代理配置能否进入 Google AI Studio 与 Gemini 的桌面工具**

以登录浏览器的实际访问结果为判定依据，批量测试代理配置能否打开 AI Studio 与 Gemini：Simple 模式测试自有配置（vless/vmess/trojan/ss 链接、订阅 URL 或 base64），Advanced 模式将免费配置链接到可用基础配置之后形成链式出口。内置反 DPI 配置文件（fragment 分片、指纹、ALPN、密码套件），支持导出 Xray 配置，提供 Windows/macOS/Linux 桌面应用、Android APK 与 Web 服务器形态；Android 仅支持连通性检测，区域检测需 Chrome/Edge/Brave。

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

- 以登录账号实际打开页面读取 Google 区域判定，而非 HTTP 连通性探测
- Simple/Advanced 双模式，支持链式配置与导出链式 Xray 配置
- 内置可编辑的反 DPI 配置（Finalmask 分片、指纹、ALPN、密码套件）
- 提供桌面/Web/Android 多形态，带 SHA256SUMS 校验

## 适用场景

- 批量筛选我手头哪条代理配置能打开 Gemini
- Cloudflare 配置连通但出口被封时，找别的出口
- 依赖该配置前先测一遍是否可用

## 场景标签

 · 领域:网络工具/代理检测

## 证据(README 行号)

> L11: Find proxy configs that actually get you into **Google AI Studio and Gemini**, by testing each one the way a person
> L43: |XTLS/Xray-core|The proxy engine embedded in the app|

## 星数曲线

```mermaid
xychart-beta
    title "Samokoto/Gemini-Config-Checker- 星数(近 2 点)"
    x-axis ["2026-11-18", "2026-11-19"]
    y-axis "stars" 61 --> 63
    line [62, 62]
```

2026-11-18 62 → 2026-11-19 62（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 mid · 依据 README sha `7d4e3e000e83` · [字段定义](../../DATASET.md)*
