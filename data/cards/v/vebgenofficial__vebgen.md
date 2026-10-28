# vebgenofficial/vebgen

⭐ 21 · Python · MIT · 推送 2025-11-01 · [GitHub](https://github.com/vebgenofficial/vebgen) · 个人维护

**AST 驱动的自然语言生成 Django/Flask 应用的 AI 开发代理**

面向需要从自然语言生成完整 Web 应用的开发者：双 Agent 架构（Tars 分析错误、Case 打补丁）最多 3 次自动修复循环；通过 AST 解析代码结构构建上下文，不将整文件送入 LLM；内置命令白名单、路径校验等沙箱机制，无需 Docker；状态持久化到 .vebgen/ 目录，含 SHA-256 校验、5 份时间戳备份与软删除回收站。支持加载非 VebGen 创建的 Django 项目。免费层 API（Gemini/OpenRouter）构建，BYOK 模式，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AST 解析 95+ 构造构建零 token 上下文
- 双 Agent（Tars+Case）自动修复循环，含断路器防死循环
- 5 层代码补丁匹配策略（精确/空白/缩进/模糊/Tree-Sitter 预留）
- 状态持久化：SHA-256 校验、5 份备份、原子写入、软删除回收站

## 适用场景

- 用自然语言从零生成 Django/Flask/React 应用
- 接手已有 Django 项目继续开发
- 在受限安全策略下让 AI 代理执行命令与修改代码

## 场景标签

 · 领域:软件开发/AI 编程代理

## 证据(README 行号)

> L29: **VebGen** is the first AI-powered development agent that **understands your code** without reading it.
> L31: While tools like Cursor and GitHub Copilot help you *write* code faster, VebGen builds **complete, production-ready
> L73: |**Full-App Generation**|✅ Django, Flask, React|❌ Code completion|❌ Code completion|✅ Full-stack|⚠️ Limited|

## 星数曲线

```mermaid
xychart-beta
    title "vebgenofficial/vebgen 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `9379942d7b69` · [字段定义](../../DATASET.md)*
