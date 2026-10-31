# SonAIengine/ku-portal-mcp

⭐ 13 · Python · MIT · 推送 2026-10-03 · [GitHub](https://github.com/SonAIengine/ku-portal-mcp) · [官网](https://pypi.org/project/ku-portal-mcp/) · 个人维护

**面向高丽大学学生的 KUPID 门户与 Canvas LMS 的 MCP 服务器**

为 Claude Code 提供 32 个 MCP tool，接入高丽大学 KUPID 门户、学事系统（AMS）与 Canvas LMS：登录无需认证即可查公告、校历、奖学金与 6 所图书馆实时座位；个人课表、成绩、开课检索需一次邮箱 OTP 二次认证（约 50 分钟有效）；LMS 部分覆盖课程、作业、资料下载与提交。通过 uvx/pip 安装，用 claude mcp add 注册并设置学号密码环境变量。2026 年学校系统迁移后 31 个 tool 中 28 个一度失效，v0.13.0–v0.17.0 已修复。

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

- 32 个 tool：公告/校历/奖学金/图书馆座位/课表/成绩/Canvas LMS 全覆盖
- 公告与图书馆座位等无需登录即可查询（公开 JSON/REST API）
- 学事查询经邮箱 6 位 OTP 二次认证，会话维持约 50 分钟
- 支持课表导出 ICS 文件、LMS 文件下载与作业提交（confirm=True 才实际提交）

## 适用场景

- 我在 Claude Code 里用自然语查询学校公告和奖学金通知
- 我查图书馆实时空座与自习室使用率
- 我查看课表、成绩、GPA 并把课表导出到日历
- 我查 Canvas LMS 作业、截止日期并提交文件型作业

## 场景标签

 · 领域:教育/校园信息系统集成

## 证据(README 行号)

> L9: 고려대학교 KUPID 포털 MCP 서버 — Claude Code에서 대학 생활에 필요한 정보를 바로 조회
> L448: |MCP|FastMCP (mcp[cli])|Claude Code 연동 프로토콜|

## 星数曲线

```mermaid
xychart-beta
    title "SonAIengine/ku-portal-mcp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 11 --> 14
    line [13, 12, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `ad94015f4bec` · [字段定义](../../DATASET.md)*
