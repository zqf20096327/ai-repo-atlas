# kerlos/pordee

⭐ 330 · JavaScript · MIT · 推送 2026-07-09 · [GitHub](https://github.com/kerlos/pordee) · 个人维护

**让 Claude Code 用泰语简短回答以减少 output token 的插件**

pordee（พอดี）是 Claude Code 插件，通过 hooks 机制让 agent 以简短泰语回答：剔除敬语词（ครับ/ค่ะ）、犹豫词与冗余连接词，保留英文技术术语，宣称可减少 60-75% output token。提供 Lite（保留完整语法）与 Full（最短化）两级，支持 slash 命令与泰语关键词触发，状态存于 ~/.pordee/state.json 跨 session 持久；/pordee-stats 统计 token 节省。遇到安全警告、不可逆命令或多步骤说明时会自动暂停简短模式。当前仅支持 Claude Code (v1)。安装提供 curl/PowerShell 一行脚本与 skills registry（npx）途径。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 通过 SessionStart/UserPromptSubmit hooks 注入简答规则并防 model drift
- Lite/Full 两级压缩，保留英文技术术语
- /pordee-stats 查看 session 与 lifetime token 节省统计
- 安全警告、不可逆命令（rm -rf、DROP TABLE 等）时自动暂停简短模式

## 适用场景

- 让 Claude Code 的泰语回答更省 token 和更易快速阅读
- 统计每次会话节省的 output token 与费用估算
- 在需要详细解释时用关键词临时切换回完整回答

## 场景标签

 · 领域:开发者工具/LLM 客户端插件

## 证据(README 行号)

> L7: `pordee` คือ Claude Code plugin สั่งให้ agent ตอบภาษาไทยกระชับ — ตัดคำสุภาพ (ครับ/ค่ะ/นะคะ), คำลังเล (อาจจะ/น่าจะ), 
> L184: 1. ติดตั้ง plugin → Claude Code register hook ของ pordee อัตโนมัติ
> L251: - ตอนนี้รองรับเฉพาะ Claude Code (v1) — โปรแกรมอื่นๆ จะเพิ่มเข้ามาในทีหลัง

## 星数曲线

```mermaid
xychart-beta
    title "kerlos/pordee 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 329 --> 331
    line [330, 330]
```

2026-10-18 330 → 2026-10-25 330（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `a9d04542194e` · [字段定义](../../DATASET.md)*
