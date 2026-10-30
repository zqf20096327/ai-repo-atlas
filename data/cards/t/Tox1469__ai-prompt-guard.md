# Tox1469/ai-prompt-guard

⭐ 18 · TypeScript · MIT · 推送 2026-10-07 · [GitHub](https://github.com/Tox1469/ai-prompt-guard) · 个人维护

**LLM 应用的提示注入检测库，按权重累计并锁定用户**

TypeScript 模式匹配库，检测 8 层提示注入攻击（数据外泄、令牌走私、直接注入、越狱、SQL、多语言变体等），每层带级别与权重，首个命中层生效。匹配前做归一化（去重音、零宽字符、西里尔/希腊同形字母、全角、base64 解码）。createGuard 提供按用户的累计计分与锁定机制，存储层可插拔（默认内存 Map 上限 1 万用户）。运行时零依赖，支持 Node 18+ 与边缘运行时。README 明确声明这是模式匹配、不理解意图，应作为第一层防护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 8 层攻击检测（英/葡语），每层带级别与权重
- 文本归一化对抗常见绕过手法，含 base64 解码检查
- 按用户计分锁定机制，存储可插拔（get/set/delete 即可）
- 零运行时依赖，可在边缘运行时运行

## 适用场景

- 在我的 LLM 聊天端点前拦截提示注入攻击
- 对反复尝试注入的用户按累计权重自动锁定
- 清理送入 prompt 的控制字符与聊天模板标记

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L6: Prompt injection detection for LLM apps, with a strike counter that locks users who keep trying.
> L28: ## What it catches

## 星数曲线

```mermaid
xychart-beta
    title "Tox1469/ai-prompt-guard 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-29", "2026-10-30"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-30 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `e5011184ab72` · [字段定义](../../DATASET.md)*
