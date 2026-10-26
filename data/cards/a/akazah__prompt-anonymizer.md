# akazah/prompt-anonymizer

⭐ 31 · TypeScript · MIT · 推送 2026-07-22 · [GitHub](https://github.com/akazah/prompt-anonymizer) · [官网](https://akazah.github.io/prompt-anonymizer/) · 个人维护 · 中文 README

**提示词发往 LLM 前的本机可逆 PII 匿名化工具**

在文本离开本机前检测并用一致占位符（如 <人名_1>）替换 PII，LLM 回复返回后依据仅在本地保留的映射还原原文。检测在本机运行：Python 端用 Presidio + spaCy NER，浏览器/桌面端用 WebGPU/WASM 与 transformers.js，Node 端默认仅正则、NER 可选。支持英日西越中等十种语言及地区化结构化 PII（日本邮编、My Number 校验位等）。交付形态覆盖 pip/npx CLI、浏览器应用、桌面应用、Chrome 扩展、Web 组件、OpenAI 兼容本地代理、MCP server 与 CI/commit 门禁（scan）。

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

- 同一值映射到同一占位符，回答保留语义且可本地还原
- 检测全程本机运行（WebGPU/WASM、spaCy、transformers.js），映射不出设备
- OpenAI 兼容反向代理：出站前脱敏、响应（含流式）中还原标签
- scan 子命令作为 git hook/CI 门禁，仅输出 file:line:col 与实体类型

## 适用场景

- 在浏览器或桌面端粘贴提示词前自动脱敏个人信息
- 让任何 OpenAI 兼容客户端经本地代理出站前脱敏 PII
- 在 commit/CI 阶段拦截误入代码或文档的 PII
- 给 Claude Desktop/Cursor 等 MCP 客户端挂载匿名化工具

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L47: Detection runs on-device (WebGPU / WASM in the browser, spaCy or local
> L155: By default detection is regex-only (emails, phone numbers, …); pass a

## 星数曲线

```mermaid
xychart-beta
    title "akazah/prompt-anonymizer 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26"]
    y-axis "stars" 29 --> 32
    line [30, 31, 31]
```

2026-10-18 30 → 2026-10-26 31（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `be504e3ce083` · [字段定义](../../DATASET.md)*
