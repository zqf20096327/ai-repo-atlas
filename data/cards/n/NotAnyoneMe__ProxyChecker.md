# NotAnyoneMe/ProxyChecker

⭐ 48 · Python · MIT · 推送 2026-09-30 · [GitHub](https://github.com/NotAnyoneMe/ProxyChecker) · 个人维护

**带 GUI 的多协议代理检测工具：批量验证 HTTP/SOCKS 代理可用性**

基于 tkinter 的 Python 桌面应用，批量检测 HTTP、HTTPS、SOCKS4、SOCKS5 代理：支持 IP:PORT、含账号密码等多种输入格式，提供 HTTP 请求与 Socket 连接两种验证方式，测量下载速度、通过 ip-api.com 做国家归属检测，结果可按多条件排序并导出 CSV/TXT。全部依赖均为 Python 标准库，需 Python 3.6+，Windows/Linux/macOS 均可运行。README 未描述任何 AI 功能（仓库虽带 ai 主题标签）。供爬虫开发者、代理管理者和网络管理员使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 HTTP/HTTPS/SOCKS4/SOCKS5 四种代理类型与多种输入格式
- 双验证方式（HTTP 请求 / Socket 连接）与下载速度测量
- IP 地理位置国家检测与去重、多条件排序
- 仅依赖 Python 标准库，无需安装额外依赖

## 适用场景

- 批量验证代理列表可用性并导出存活代理
- 为爬虫或自动化任务筛选可用的代理
- 测量代理速度与归属国家做管理决策

## 场景标签

 · 领域:网络工具/代理管理

## 证据(README 行号)

> L10: A professional, feature-rich proxy checker application with a modern dark-themed GUI. Test HTTP, HTTPS, SOCKS4, and
> L58: All required libraries are part of Python's standard library:

## 星数曲线

```mermaid
xychart-beta
    title "NotAnyoneMe/ProxyChecker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 47 --> 49
    line [48, 48]
```

2026-10-18 48 → 2026-10-31 48（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 low · 依据 README sha `72a9843fff57` · [字段定义](../../DATASET.md)*
