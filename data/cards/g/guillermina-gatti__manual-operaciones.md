# guillermina-gatti/manual-operaciones

⭐ 3 · TypeScript · MIT · 推送 2026-11-26 · [GitHub](https://github.com/guillermina-gatti/manual-operaciones) · 组织维护

**企业内部操作手册平台，RAG 助手引用内部文档作答**

面向企业的交互式操作手册 Web 平台：按角色（管理员/主管/员工）与部门隔离内容，员工按步骤浏览流程并记录进度，上传 PDF 与文本文档后由 RAG 助手作答，仅基于内部手册并在模型看到内容前于数据库层按权限过滤，回答附来源文档引用。认证采用短期 access token 加轮换 refresh token。课程期末项目，由 6 人团队开发，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- RAG 助手仅基于内部手册作答并引用来源文档
- 模型读取前在数据库层按权限过滤内容
- PDF 与文本文档上传处理
- 角色与部门维度的内容隔离

## 适用场景

- 让新员工按部门查看操作流程并逐步执行
- 用 AI 助手查询内部手册并获得出处引用
- 按角色权限控制文档与流程的可见范围

## 场景标签

`RAG` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L5: consultar a un asistente de IA que responde usando únicamente los manuales
> L16: - Asistente con RAG: respuestas con cita a la fuente y filtrado por permisos
> L26: |IA|Amazon Bedrock|

## 星数曲线

```mermaid
xychart-beta
    title "guillermina-gatti/manual-operaciones 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-28"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-08 3 → 2026-11-28 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `ae0dd33c4e61` · [字段定义](../../DATASET.md)*
