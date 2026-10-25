# airmang/python-hwpx-automation

⭐ 68 · Python · Apache-2.0 · 推送 2026-10-15 · [GitHub](https://github.com/airmang/python-hwpx-automation) · [官网](https://pypi.org/project/hwpx-mcp-server/) · 个人维护 · 中文 README

**供 AI agent 读写编辑 HWPX 韩文文档的 Python 层与 MCP 服务器**

构建在 python-hwpx 引擎之上的应用层：提供文档创作、表单填写、试卷排版等 Python API 与 hwpx CLI，MCP 服务器通过 [mcp] extra 可选安装，供 Claude Desktop、VS Code、Gemini CLI、Cursor 等 MCP 客户端的 AI agent 调用。提供读取导航、搜索替换、原子化编辑（dry-run/回滚/幂等键）、表单填写三步事务、邮件合并、PDF 渲染等工具；保存经单一 SavePipeline 校验门，工作区路径限制防 traversal，无需韩文 Office 或 Windows，Python>=3.10。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 声明式 create_document_from_plan 与公文规范 lint
- 表单填写 analyze→apply→verify 的字节保留事务
- 编辑支持 dry-run、回滚、幂等键与变更追踪
- MCP 服务器可配 Claude Desktop/VS Code/Gemini CLI/Cursor 等，工作区根目录限制

## 适用场景

- 让 Claude 等 AI agent 在本地安全修改 HWPX 文档
- Python 脚本批量生成与填写 HWPX 表单
- 将 HWPX/非 HWPX 文档转为 Markdown 供 agent 读取

## 场景标签

`文档解析` `AI 写作` · 领域:内容生成

## 证据(README 行号)

> L19: 기본 설치는 MCP 없이 Python API와 `hwpx` CLI로 쓰고,
> L20: 모델 컨텍스트 프로토콜(MCP) 서버는 필요할 때
> L27: |🔌|`python-hwpx-automation`|저작·양식 채움 워크플로, `hwpx` CLI, 선택형 MCP 서버|

## 星数曲线

```mermaid
xychart-beta
    title "airmang/python-hwpx-automation 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 67 --> 69
    line [68, 68]
```

2026-10-18 68 → 2026-10-25 68（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `8fe7bcd4c9ca` · [字段定义](../../DATASET.md)*
