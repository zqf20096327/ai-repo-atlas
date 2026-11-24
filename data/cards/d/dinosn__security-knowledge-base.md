# dinosn/security-knowledge-base

⭐ 10 · Python · MIT · 推送 2026-08-12 · [GitHub](https://github.com/dinosn/security-knowledge-base) · 个人维护

**本地优先的安全知识库模板：AI 可读检索，人工审核变更**

以 Git+JSON+Markdown+Python 标准库 CLI 构建的安全知识库框架模板：收录安全发现、声明、被否决假设、来源出处与审核决策，原始证据不可变且内容寻址，摄入只存储字节与出处、从不执行；模型可通过统一的离线 JSON CLI 读取/搜索，其唯一写权限是经校验的 proposals 文件，生成分析须人工按摘要批准后才成为正式记录。仓库本身为空框架与公开数据模板，运营数据须另建私有仓库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 跨模型 Agent Skill：gh 一条命令安装到 Codex/Claude Code/Gemini CLI 等宿主
- 模型唯一写路径为 proposals/，须人工批准摘要后经 CLI 提升
- 无需供应商 API、MCP、向量库或网络；核心零第三方 Python 依赖
- 提示注入风险内建处理：证据视为不可信字节，确定性词法搜索

## 适用场景

- 为安全调查建立可审计的证据与结论知识库
- 让多个 agent 宿主在同一受控仓库上读写安全研究记录
- 在无网络、无向量库环境下做威胁猎杀资料管理

## 场景标签

`网络安全` `知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L3: A local-first, evidence-led repository for security findings, claims, rejected
> L45: Installing the skill installs only the model-neutral operating procedure. It
> L147: Agents can read and search, but their only repository write is a validated file

## 星数曲线

```mermaid
xychart-beta
    title "dinosn/security-knowledge-base 星数(近 2 点)"
    x-axis ["2026-10-21", "2026-11-24"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-21 10 → 2026-11-24 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `dea3f9b819bc` · [字段定义](../../DATASET.md)*
